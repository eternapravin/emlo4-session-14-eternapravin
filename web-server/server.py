import os
import zlib
import json
import logging
import socket

import redis.asyncio as redis
import httpx
import base64

from fastapi import FastAPI, File, Depends, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from fastapi.responses import Response
from typing import Annotated

# Configure logging
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - WebServer - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

app = FastAPI(title="Web Server")

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Add constants
HOSTNAME = socket.gethostname()
REDIS_HOST = os.environ.get("REDIS_HOST", "localhost")
REDIS_PORT = os.environ.get("REDIS_PORT", "6379")
REDIS_PASSWORD = os.environ.get("REDIS_PASSWORD", "")
MODEL_SERVER_URL = os.environ.get("MODEL_SERVER_URL", "http://localhost:8000")

@app.on_event("startup")
async def initialize():
    global redis_pool
    logger.info(f"Initializing web server on host {HOSTNAME}")
    logger.info(f"Creating Redis connection pool: host={REDIS_HOST}, port={REDIS_PORT}")
    redis_pool = redis.ConnectionPool(
        host=REDIS_HOST,
        port=REDIS_PORT,
        password=REDIS_PASSWORD,
        db=0,
        decode_responses=True,
    )
    logger.info("Web server initialization complete")

@app.on_event("shutdown")
async def shutdown():
    """Cleanup connection pool on shutdown"""
    logger.info("Shutting down web server")
    await redis_pool.aclose()
    logger.info("Cleanup complete")

def get_redis():
    return redis.Redis(connection_pool=redis_pool)

async def check_cached(image: bytes):
    hash = zlib.adler32(image)
    cache = get_redis()

    logger.debug(f"Checking cache for image hash: {hash}")
    data = await cache.get(hash)

    if data:
        logger.info(f"Cache hit for image hash: {hash}")
    else:
        logger.info(f"Cache miss for image hash: {hash}")

    return json.loads(data) if data else None

@app.post("/classify")
async def classify_imagenet(image: Annotated[bytes, File()]):
    """
    Handles image classification requests by checking the cache first.
    If not cached, forwards the request to the model server.
    """
    logger.info("Received classification request")
    infer_cache = await check_cached(image)

    if infer_cache is None:
        logger.info("Cache miss. Making request to model server.")
        async with httpx.AsyncClient() as client:
            try:
                # Construct the URL for the model server's classify endpoint
                url = f"{MODEL_SERVER_URL}/classify"

                # Send the image as multipart/form-data
                files = {"file": ("image.jpg", image, "image/jpeg")}
                logger.debug(f"Sending request to model server: {url}")

                response = await client.post(url, files=files)

                # Raise an exception if the response status code is not 2xx
                response.raise_for_status()

                # Log and return the model server's response
                logger.info("Successfully received model prediction")
                return response.json()
            except Exception as e:
                # Log the error and raise an HTTPException for the client
                logger.error(f"Model server request failed: {str(e)}")
                raise HTTPException(status_code=500, detail="Error from Model Endpoint")

    # If the result is cached, return it
    logger.info("Returning cached result")
    return infer_cache


@app.get("/health")
async def health_check():
    """Health check endpoint for kubernetes readiness/liveness probes"""
    try:
        # Test Redis connection
        redis_client = get_redis()
        redis_connected = await redis_client.ping()
    except Exception as e:
        logger.error(f"Redis health check failed: {str(e)}")
        redis_connected = False

    try:
        # Test Model Server connection
        async with httpx.AsyncClient() as client:
            response = await client.get(f"{MODEL_SERVER_URL}/health")
            response.raise_for_status()
            model_health = response.json()
            model_connected = True
    except Exception as e:
        logger.error(f"Model server health check failed: {str(e)}")
        model_connected = False
        model_health = None

    health_status = {
        "status": "healthy" if (redis_connected and model_connected) else "degraded",
        "hostname": HOSTNAME,
        "redis": {"host": REDIS_HOST, "port": REDIS_PORT, "connected": redis_connected},
        "model_server": {
            "url": MODEL_SERVER_URL,
            "connected": model_connected,
            "health": model_health,
        },
    }

    logger.info(f"Health check status: {health_status['status']}")
    return health_status

# uvicorn server:app --host 0.0.0.0 --port 9000 --reload