Name:                   model-server
Namespace:              dev
CreationTimestamp:      Fri, 21 Mar 2025 05:50:08 +0000
Labels:                 app.kubernetes.io/managed-by=Helm
                        app.kubernetes.io/name=model-server
                        app.kubernetes.io/part-of=fastapi-app
Annotations:            deployment.kubernetes.io/revision: 1
                        meta.helm.sh/release-name: fastapi-release-dev
                        meta.helm.sh/release-namespace: dev
Selector:               app.kubernetes.io/name=model-server
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app.kubernetes.io/name=model-server
  Containers:
   model-server:
    Image:      model-server:latest
    Port:       8000/TCP
    Host Port:  0/TCP
    Limits:
      cpu:     1
      memory:  2Gi
    Environment:
      REDIS_HOST:      <set to the key 'hostname' of config map 'redis-config-v1'>           Optional: false
      REDIS_PORT:      <set to the key 'port' of config map 'redis-config-v1'>               Optional: false
      REDIS_PASSWORD:  <set to the key 'db_password' in secret 'redis-secret-v1'>            Optional: false
      MODEL_NAME:      <set to the key 'model_name' of config map 'model-server-config-v1'>  Optional: false
    Mounts:            <none>
  Volumes:             <none>
  Node-Selectors:      <none>
  Tolerations:         <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Progressing    True    NewReplicaSetAvailable
  Available      True    MinimumReplicasAvailable
OldReplicaSets:  <none>
NewReplicaSet:   model-server-588897c84c (1/1 replicas created)
Events:          <none>
Name:                   redis
Namespace:              dev
CreationTimestamp:      Fri, 21 Mar 2025 05:50:08 +0000
Labels:                 app.kubernetes.io/managed-by=Helm
                        app.kubernetes.io/name=redis
                        app.kubernetes.io/part-of=fastapi-app
Annotations:            deployment.kubernetes.io/revision: 1
                        meta.helm.sh/release-name: fastapi-release-dev
                        meta.helm.sh/release-namespace: dev
Selector:               app.kubernetes.io/name=redis,role=master
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app.kubernetes.io/name=redis
           role=master
  Containers:
   redis:
    Image:      redis:7.4.1
    Port:       6379/TCP
    Host Port:  0/TCP
    Command:
      redis-server
    Args:
      --requirepass
      $(REDIS_PASSWORD)
    Limits:
      cpu:     200m
      memory:  200Mi
    Environment:
      REDIS_PASSWORD:  <set to the key 'db_password' in secret 'redis-secret-v1'>  Optional: false
    Mounts:
      /data from redis-storage (rw)
  Volumes:
   redis-storage:
    Type:          PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:     redis-pvc
    ReadOnly:      false
  Node-Selectors:  <none>
  Tolerations:     <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Progressing    True    NewReplicaSetAvailable
  Available      True    MinimumReplicasAvailable
OldReplicaSets:  <none>
NewReplicaSet:   redis-6cb764f4b8 (1/1 replicas created)
Events:          <none>
Name:                   web-server
Namespace:              dev
CreationTimestamp:      Fri, 21 Mar 2025 05:50:08 +0000
Labels:                 app.kubernetes.io/managed-by=Helm
                        app.kubernetes.io/name=web-server
                        app.kubernetes.io/part-of=fastapi-app
Annotations:            deployment.kubernetes.io/revision: 1
                        meta.helm.sh/release-name: fastapi-release-dev
                        meta.helm.sh/release-namespace: dev
Selector:               app.kubernetes.io/name=web-server
Replicas:               1 desired | 1 updated | 1 total | 1 available | 0 unavailable
StrategyType:           RollingUpdate
MinReadySeconds:        0
RollingUpdateStrategy:  25% max unavailable, 25% max surge
Pod Template:
  Labels:  app.kubernetes.io/name=web-server
  Containers:
   web-server:
    Image:      web-server:latest
    Port:       80/TCP
    Host Port:  0/TCP
    Environment:
      REDIS_HOST:        <set to the key 'hostname' of config map 'redis-config-v1'>                 Optional: false
      REDIS_PORT:        <set to the key 'port' of config map 'redis-config-v1'>                     Optional: false
      REDIS_PASSWORD:    <set to the key 'db_password' in secret 'redis-secret-v1'>                  Optional: false
      MODEL_SERVER_URL:  <set to the key 'model_server_url' of config map 'model-server-config-v1'>  Optional: false
    Mounts:              <none>
  Volumes:               <none>
  Node-Selectors:        <none>
  Tolerations:           <none>
Conditions:
  Type           Status  Reason
  ----           ------  ------
  Progressing    True    NewReplicaSetAvailable
  Available      True    MinimumReplicasAvailable
OldReplicaSets:  <none>
NewReplicaSet:   web-server-55bc6c44bc (1/1 replicas created)
Events:          <none>
