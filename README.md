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
  - Created 2 applications - model-server and web-server, model-server contains the necessary code to do the inferencing of cat-dog classifier and web interfacce to access the model-server was 
    abstracted to web-server
  - Web-server should be configured with NodePort with applicable port number equal or above 30000 to enable external hosting and enable using public IP address of the Ec2 instance for hosting, redis 
    and model-server can continue with the type 'clusterIP' as those applications will not have any external interface unline web-server.
  - Build and deploy Instructions:
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
  - Test instructions: 
    - All the pods, meant for web-server, model-server and redis should be in 'running' status, before testing the application
    - Now, run the web-server service using the command: `minikube service web-server-service`
    - Enable tunneling using `minikube tunnel`
    - Apply port forwarding using the command: `kubectl port-forward service/web-server-service 30000:80 --address=0.0.0.0 -n default`
    -  Open the web-browser with the public IP address of the Ec2 instance (as we have hosted the minikube and the application on the Ec2 instance) in your local machine as
       http://43.205.96.203:30000/docs#/
    - Hit the the Health and classify end-points to test the application deployed on kubernetes using try it out button, for successful operation, you will find the below output:
      ![image](https://github.com/user-attachments/assets/783e9f38-899d-40e9-b22d-e5358d097450)
      ![image](https://github.com/user-attachments/assets/f02d87d2-fc55-4586-92c1-bebdb59172ad)
    - Once the test is complete using kubectl, the same application be deployed using Helm Chart by the below steps
       - Run this command: `helm create fastapi-helm`
       - Delete all files inside templates and clear out values.yaml
       - Copy all the .yaml template files and copy inside templates folder of our chart
       - You should be good to deploy this as is!
       - Run the command:  `helm install fastapi-release fastapi-helm/ `
       - Test this the same way by using the Test instruction given above.
    - We can optimize the config files using a more generic framework through usage of values.yaml file where in use the values.yaml file to collate all the configurable parameters in one place and refer the values.yaml file in all other yaml files, this avoids duplication of the same configuration as well as it reduces human errors to the maximum.
    - We can this way scale up this configurations for different environments or different namespaces, for example we can create values-dev.yaml and values-prod.yaml for namespace specific configurations and we can run the application in all the environments/namespaces individually without conflicting the resource requirements.
    -  multiple namespaces can be created like dev and prod in additon to the default namespace using
       `kubectl create namespace dev`
       `kubectl create namespace prod`
    - As the default namespace is pre-existed and was managed by Kubernetes and not helm, we may need to add required annotations and labels as below:
      
       ` kubectl label namespace default app.kubernetes.io/managed-by=Helm --overwrite`
      
       ` kubectl annotate namespace default meta.helm.sh/release-name=fastapi-release-default --overwrite`
      
       ` kubectl annotate namespace default meta.helm.sh/release-namespace=default --overwrite`
      
     - The Helm chart is installed by the following command for default namespace as:
     - helm install fastapi-release-default fastapi-helm --values fastapi-helm/values.yaml --namespace default
      - The Helm chart for namespaces dev and prod be installed by the following commands below:
      - DEV: 
       ` kubectl label namespace dev app.kubernetes.io/managed-by=Helm --overwrite`
      
       ` kubectl annotate namespace dev meta.helm.sh/release-name=fastapi-release-dev --overwrite`
      
       ` kubectl annotate namespace dev meta.helm.sh/release-namespace=dev --overwrite`
    
       ` helm install fastapi-release-dev fastapi-helm --values fastapi-helm/values.yaml -f fastapi-helm/values-dev.yaml --namespace dev `
      - PROD:
       ` kubectl label namespace prod app.kubernetes.io/managed-by=Helm --overwrite`
      
       ` kubectl annotate namespace prod meta.helm.sh/release-name=fastapi-release-prod --overwrite`
      
       ` kubectl annotate namespace prod meta.helm.sh/release-namespace=prod --overwrite`

       ` helm install fastapi-release-prod fastapi-helm --values fastapi-helm/values.yaml -f fastapi-helm/values-prod.yaml --namespace prod `

    - Once deployed using Helm chart, the successful deployment will get a simmilar following prompt message in the console
      ![image](https://github.com/user-attachments/assets/8897d041-6b90-4bb4-917b-39e50d8d0627)

   
    - 
    - 

        
