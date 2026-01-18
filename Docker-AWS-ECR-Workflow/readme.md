# Hello Flask – Docker, Networking & Cloud Container Workflow

## Overview

This project is a core DevOps learning milestone focused on **containerising applications, managing container networking, optimising images, and publishing images to cloud registries**.

The goal was not application complexity, but to demonstrate:
- Real Docker workflows
- Container networking fundamentals
- Image optimisation and lifecycle management
- Cloud registry integration (AWS ECR)
- Operational hygiene and performance awareness

This project goes beyond a basic “hello world” container and reflects **production-minded DevOps practices**.

---

## Application Description

The application is a simple Python Flask web application that:
- Runs inside a Docker container
- Exposes an HTTP endpoint
- Is used to validate container builds, networking, and registry workflows

---

## Technologies Used

- Python (Flask)
- Docker
- Docker Desktop
- AWS (ECR, IAM, STS)
- Docker Hub
- AWS CLI

---

## Project Structure

hello_flask/
├── Dockerfile
├── app.py
├── requirements.txt
└── README.md

## Containerisation

The application was containerised using a Dockerfile that:

Uses a lightweight Python base image

Copies application files into the container

Installs dependencies

Exposes the application port

Starts the Flask application

The result is a fully portable and reproducible containerised service.

Image Build & Local Testing

## The Docker image was built locally:

Bash:
docker build -t hello-flask .

The container was run and tested locally:

Bash:
docker run -d -p 5002:5002 hello-flask

Successful access via browser confirmed:
Correct port mapping
Application running inside the container

## Custom Docker Networking

A custom Docker bridge network was created to explicitly control communication between the Flask application and the database container.

Bash:
docker network create my-app-network


Containers were attached to this network, allowing services to communicate using container names rather than relying on default networking behaviour.

This reinforced understanding of:
Docker networking fundamentals
Container DNS and name resolution
Explicit service isolation and connectivity

## AWS ECR Integration

This project includes end-to-end integration with Amazon Elastic Container Registry (ECR).

## Steps Completed:

Configured AWS CLI locally
Verified AWS authentication using STS
Created an ECR repository
Authenticated Docker against AWS ECR
Tagged images correctly for ECR
Pushed images to the cloud registry

Authentication was verified using:

Bash:
aws sts get-caller-identity

## Docker Login to ECR

Docker was authenticated with AWS ECR using:
Bash:
aws ecr get-login-password --region <region> \
| docker login --username AWS --password-stdin <account_id>.dkr.ecr.<region>.amazonaws.com


Successful login confirmed secure registry access.

## Image Tagging & Push to ECR

The local image was tagged and pushed to ECR:

Bash:
docker tag hello-flask:latest <account_id>.dkr.ecr.<region>.amazonaws.com/hello-flask:latest
docker push <account_id>.dkr.ecr.<region>.amazonaws.com/hello-flask:latest


This validated:
Image tagging conventions
Registry authentication
Cloud image storage

## Dockerfile Optimisation & Image Size Reduction

The Dockerfile was refactored to improve performance and reduce image size.

## Before optimisation

Image sizes close to ~1GB / ~450MB
Slower build times
Higher disk usage

## After optimisation
Slimmer base images and refactoring applied
Unnecessary build artifacts removed
Significantly reduced image size
Faster build and startup times

This mirrors real-world production best practices, where image size and performance directly affect CI/CD speed and infrastructure costs.

## Image & Container Cleanup

Docker Desktop was used to:
Remove unused containers
Remove unused images
Free disk space and storage

This reinforced the importance of:
Container lifecycle management
Maintaining a clean local development environment
Resource awareness in container-heavy workflows

## What I Learned
How Docker containers isolate applications and dependencies
Writing and optimising Dockerfiles
Managing Docker images and registries
Creating and using custom Docker networks
Authenticating Docker with AWS ECR
Image tagging, pushing, and verification workflows
Reducing image size for performance and efficiency
Operational cleanup and disk management

## Challenges & Solutions
**Docker authentication issues**
Solved by configuring AWS CLI correctly and verifying identity with STS.

**Image size bloat**
Solved by refactoring the Dockerfile and using lighter base images.

**Container networking confusion**
Solved by creating a custom Docker network and explicitly attaching services.

## Docker Commands Practised/Used

# Build Docker image
docker build -t hello-flask .

# Run container locally
docker run -d -p 5002:5002 hello-flask

# List images and containers
docker images
docker ps
docker ps -a

# Docker networking
docker network create my-app-network
docker network ls

# Authenticate with AWS
aws configure
aws sts get-caller-identity

# Login to AWS ECR
aws ecr get-login-password --region <region> \
| docker login --username AWS --password-stdin <account_id>.dkr.ecr.<region>.amazonaws.com

# Tag and push image to ECR
docker tag hello-flask:latest <account_id>.dkr.ecr.<region>.amazonaws.com/hello-flask:latest
docker push <account_id>.dkr.ecr.<region>.amazonaws.com/hello-flask:latest

## **Final Note**

This project represents a significant step in my DevOps learning journey, moving beyond local containerisation into networked services, image optimisation, and cloud registry workflows.

It forms a strong foundation for:
CI/CD pipelines
AWS ECS deployments
Kubernetes image pulls
Production-grade container systems