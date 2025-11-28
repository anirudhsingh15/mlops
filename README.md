# End-to-End MLOps: Dockerized Inference API on Kubernetes

**Objective:** Designed and deployed a production-ready Machine Learning API for real-time inference, containerized with Docker and orchestrated on a Kubernetes cluster.
The Engineering Challenge: Moving a model from a Jupyter Notebook to a scalable, isolated production environment that can handle traffic and recover from failures.

**Tech Stack**
* Model: Scikit-Learn (Logistic Regression).

* API Framework: FastAPI (Python 3.11).

* Containerization: Docker (Multi-stage build).

* Orchestration: Kubernetes (Minikube), Kubectl.

* Documentation: Swagger UI (Auto-generated).

**Architecture**

* Model Training: A robust pipeline trains and serializes the model (.pkl).

* API Layer: FastAPI loads the model on startup and provides a strictly typed /predict endpoint using Pydantic validation.

* Container Layer: A lightweight Docker image encapsulates the environment, ensuring consistency across dev and prod.

* Orchestration: Kubernetes manages the deployment, handling Service Discovery (LoadBalancer) and Replica Management.

**How to Run Locally (Docker)**
```
# Build the image
docker build -t mlops-api:v1 .

# Run the container
docker run -p 8000:8000 mlops-api:v1
```

**How to Deploy (Kubernetes)**
```
# 1. Start Minikube
minikube start

# 2. Build image inside cluster context
eval $(minikube docker-env)
docker build -t mlops-api:v1 .

# 3. Apply Manifests
kubectl apply -f deployment.yaml
kubectl apply -f service.yaml

# 4. Access Service
minikube service mlops-service
```

**Key Files**

* main.py: The production API code with Pydantic validation.

* Dockerfile: The container specification.

* deployment.yaml: Kubernetes Deployment manifest defining the replica set.

* service.yaml: Kubernetes Service manifest exposing the network interface.
