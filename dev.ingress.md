Name:             web-server-ingress
Labels:           app.kubernetes.io/managed-by=Helm
                  app.kubernetes.io/name=web-server
                  app.kubernetes.io/part-of=fastapi-app
Namespace:        dev
Address:          
Ingress Class:    <none>
Default backend:  <default>
Rules:
  Host                   Path  Backends
  ----                   ----  --------
  fastapi.dev.localhost  
                         /   web-server-service:80 (10.244.0.159:80)
Annotations:             meta.helm.sh/release-name: fastapi-release-dev
                         meta.helm.sh/release-namespace: dev
Events:                  <none>
