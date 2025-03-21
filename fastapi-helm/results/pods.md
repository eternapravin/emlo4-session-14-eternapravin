Name:             model-server-588897c84c-bzcm9
Namespace:        dev
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Fri, 21 Mar 2025 05:50:08 +0000
Labels:           app.kubernetes.io/name=model-server
                  pod-template-hash=588897c84c
Annotations:      <none>
Status:           Running
IP:               10.244.0.158
IPs:
  IP:           10.244.0.158
Controlled By:  ReplicaSet/model-server-588897c84c
Containers:
  model-server:
    Container ID:   docker://4a5a2d0d1c47d21f5403eaece43a3326758227b3a44e0606753dbbd8ff6743aa
    Image:          model-server:latest
    Image ID:       docker://sha256:63d50778d4a8c662a6fe762e5789f0bd166cc38ecbf9eeae44a232115ae158cd
    Port:           8000/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Fri, 21 Mar 2025 07:59:54 +0000
    Last State:     Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 21 Mar 2025 05:50:09 +0000
      Finished:     Fri, 21 Mar 2025 07:38:52 +0000
    Ready:          True
    Restart Count:  1
    Limits:
      cpu:     1
      memory:  2Gi
    Requests:
      cpu:     1
      memory:  2Gi
    Environment:
      REDIS_HOST:      <set to the key 'hostname' of config map 'redis-config-v1'>           Optional: false
      REDIS_PORT:      <set to the key 'port' of config map 'redis-config-v1'>               Optional: false
      REDIS_PASSWORD:  <set to the key 'db_password' in secret 'redis-secret-v1'>            Optional: false
      MODEL_NAME:      <set to the key 'model_name' of config map 'model-server-config-v1'>  Optional: false
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-pbgzt (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-pbgzt:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Guaranteed
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason          Age   From     Message
  ----    ------          ----  ----     -------
  Normal  SandboxChanged  56m   kubelet  Pod sandbox changed, it will be killed and re-created.
  Normal  Pulled          56m   kubelet  Container image "model-server:latest" already present on machine
  Normal  Created         56m   kubelet  Created container: model-server
  Normal  Started         56m   kubelet  Started container model-server
Name:             redis-6cb764f4b8-6kvgf
Namespace:        dev
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Fri, 21 Mar 2025 05:50:08 +0000
Labels:           app.kubernetes.io/name=redis
                  pod-template-hash=6cb764f4b8
                  role=master
Annotations:      <none>
Status:           Running
IP:               10.244.0.157
IPs:
  IP:           10.244.0.157
Controlled By:  ReplicaSet/redis-6cb764f4b8
Containers:
  redis:
    Container ID:  docker://db6ebc600a34a0f4925c4302d4020ad1c1400bb9dafda0b2db07b420a19b6880
    Image:         redis:7.4.1
    Image ID:      docker-pullable://redis@sha256:bb142a9c18ac18a16713c1491d779697b4e107c22a97266616099d288237ef47
    Port:          6379/TCP
    Host Port:     0/TCP
    Command:
      redis-server
    Args:
      --requirepass
      $(REDIS_PASSWORD)
    State:          Running
      Started:      Fri, 21 Mar 2025 07:59:53 +0000
    Last State:     Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 21 Mar 2025 05:50:09 +0000
      Finished:     Fri, 21 Mar 2025 07:38:52 +0000
    Ready:          True
    Restart Count:  1
    Limits:
      cpu:     200m
      memory:  200Mi
    Requests:
      cpu:     200m
      memory:  200Mi
    Environment:
      REDIS_PASSWORD:  <set to the key 'db_password' in secret 'redis-secret-v1'>  Optional: false
    Mounts:
      /data from redis-storage (rw)
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-85vdj (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  redis-storage:
    Type:       PersistentVolumeClaim (a reference to a PersistentVolumeClaim in the same namespace)
    ClaimName:  redis-pvc
    ReadOnly:   false
  kube-api-access-85vdj:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   Guaranteed
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason          Age   From     Message
  ----    ------          ----  ----     -------
  Normal  SandboxChanged  56m   kubelet  Pod sandbox changed, it will be killed and re-created.
  Normal  Pulled          56m   kubelet  Container image "redis:7.4.1" already present on machine
  Normal  Created         56m   kubelet  Created container: redis
  Normal  Started         56m   kubelet  Started container redis
Name:             web-server-55bc6c44bc-d67c5
Namespace:        dev
Priority:         0
Service Account:  default
Node:             minikube/192.168.49.2
Start Time:       Fri, 21 Mar 2025 05:50:08 +0000
Labels:           app.kubernetes.io/name=web-server
                  pod-template-hash=55bc6c44bc
Annotations:      <none>
Status:           Running
IP:               10.244.0.159
IPs:
  IP:           10.244.0.159
Controlled By:  ReplicaSet/web-server-55bc6c44bc
Containers:
  web-server:
    Container ID:   docker://3d12859c545838bda2e1e1cf6a6499640f09634fbdd1d7dc9ca93e3af8c866a8
    Image:          web-server:latest
    Image ID:       docker://sha256:6ee8c7edd8478068f066ce02f4a5f814fb983b07bff0d8ad5b1227b9ea91832f
    Port:           80/TCP
    Host Port:      0/TCP
    State:          Running
      Started:      Fri, 21 Mar 2025 07:59:54 +0000
    Last State:     Terminated
      Reason:       Completed
      Exit Code:    0
      Started:      Fri, 21 Mar 2025 05:50:09 +0000
      Finished:     Fri, 21 Mar 2025 07:38:54 +0000
    Ready:          True
    Restart Count:  1
    Environment:
      REDIS_HOST:        <set to the key 'hostname' of config map 'redis-config-v1'>                 Optional: false
      REDIS_PORT:        <set to the key 'port' of config map 'redis-config-v1'>                     Optional: false
      REDIS_PASSWORD:    <set to the key 'db_password' in secret 'redis-secret-v1'>                  Optional: false
      MODEL_SERVER_URL:  <set to the key 'model_server_url' of config map 'model-server-config-v1'>  Optional: false
    Mounts:
      /var/run/secrets/kubernetes.io/serviceaccount from kube-api-access-7gxfd (ro)
Conditions:
  Type                        Status
  PodReadyToStartContainers   True 
  Initialized                 True 
  Ready                       True 
  ContainersReady             True 
  PodScheduled                True 
Volumes:
  kube-api-access-7gxfd:
    Type:                    Projected (a volume that contains injected data from multiple sources)
    TokenExpirationSeconds:  3607
    ConfigMapName:           kube-root-ca.crt
    ConfigMapOptional:       <nil>
    DownwardAPI:             true
QoS Class:                   BestEffort
Node-Selectors:              <none>
Tolerations:                 node.kubernetes.io/not-ready:NoExecute op=Exists for 300s
                             node.kubernetes.io/unreachable:NoExecute op=Exists for 300s
Events:
  Type    Reason          Age   From     Message
  ----    ------          ----  ----     -------
  Normal  SandboxChanged  56m   kubelet  Pod sandbox changed, it will be killed and re-created.
  Normal  Pulled          56m   kubelet  Container image "web-server:latest" already present on machine
  Normal  Created         56m   kubelet  Created container: web-server
  Normal  Started         56m   kubelet  Started container web-server
