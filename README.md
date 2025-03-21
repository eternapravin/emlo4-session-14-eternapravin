# emlo4-session-14-eternapravin

Session14 - Kubernetes - II: Ingress, ConfigMap, Secrets, Volumes and HELM


### Contents
  - [Requirements]
  - [Step-by-step-Approach-in-Development]
  - [Observation]
  - [Results]

### Requirements

1. Design a deployment to deploy the Cat/Dog or Dog Classifier on K8S
    You must first create a architecture diagram and show all pods, replicasets, deployments, service, ingress, volumes and nodes that will be involved in this deployment
    Use diagrams.netLinks to an external site. for the diagram
    write the code for model server, web server and test it with docker-compose first
    you must be using a redis cache for inference results caching
    create k8s manifests for the same
    You’ll need to figure out the peak cpu and memory usage with kubectl top pod
2. Deploy on K8S using the manifests
3. Create HELM Chart with configurable values
4. Deploy with HELM
5. You must use minikube either on your local machine or on an EC2 instance
6. What to Submit?
   Github Repo with Deployment YAML Files
   Instructions to
      Deploy using HELM Chart
      Tunnel to the Ingress
      Screenshot of the fastapi docs page with one inference done
   Output of the following in a .md file in your repository
      kubectl describe <your_deployment>
      kubectl describe <your_pod>
      kubectl describe <your_ingress>
      kubectl top pod
      kubectl top node
      kubectl get all -A -o yaml

### Step-by-step-Approach-in-Development
  - As per the choices listed in the requirement, I had chosen to create a Minikube cluster on a t3.large EC2 cluster to accomodate multiple Model inferencing for 3 environments - default, dev and prod
  - As per the requirement, Cat-Dog classifiecation model was used for this assignment
  - Fastapi framework was used for serving at port 8000
  - EC2 side configuration to be done
    - Go to the Ec2 instance, click on the security tab of the insance and select the "security group" and clock on "edit inbound rules" and add the rules as per given below:
     ![image](https://github.com/user-attachments/assets/97d537e9-e939-44e2-839e-36a78acc0c8e)
  - Created 2 applications - model-server and web-server, model-server contains the necessary code to do the inferencing of cat-dog classifier and web interfacce to access the model-server was abstracted to web-server
  - Build Instructions:
    -  To configure shell to use the Docker daemon inside Minikube instead of the default Docker daemon on the local machine, the below command was used:
       `eval $(minikube docker-env`
    - Build the model-server using this below command:
        `docker build --platform linux/amd64 -t model-server model-server`
    - Build the web-server using the below command:
        `docker build --platform linux/amd64 -t web-server web-server`
    - To come of the Docker daemon shell inside the minikube, use the following command:
         `eval $(minikube docker-env -u)`
    - The yaml configuration files were created for configmap, deployment, service for moel-server, web-server and redis and redis.volume was created for persistent volume and persisten volume claim

  - Initially the Code was tested by deploying the application using yaml configuration files using the command below:
          `kubectl apply -f .`
    
