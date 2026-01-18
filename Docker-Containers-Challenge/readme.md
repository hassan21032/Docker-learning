# Docker & Containers Challenge – Flask & Redis

## Overview

This project completes the **Docker & Containers Challenge**, where the goal was to build and run a multi-container application using Docker Compose.

The application consists of:
- A Python Flask web application
- A Redis database used as a key-value store
- Dockerfiles and Docker Compose for orchestration

---

## Application Features

- `/` – Displays a welcome message
- `/count` – Increments and displays a visit count stored in Redis

Redis is used to persist the visit count across requests.

---

## Technologies Used

- Python (Flask)
- Redis
- Docker
- Docker Compose

---

## Project Structure

redis-app/
├── Dockerfile
├── docker-compose.yml
├── app.py
├── requirements.txt
└── README.md

---

## How to Run the Application

### Prerequisites
- Docker installed
- Docker Compose available

### Steps

From the project directory, run:

Bash
docker compose up 

Then open your browser:

http://localhost:5000
 → Welcome page

http://localhost:5000/count
 → Visit counter (increments on refresh)

Docker Compose Setup

The application uses two services:

web – Flask application built from a Dockerfile

redis – Redis database using the official Redis image

A named Docker volume is used to persist Redis data across container restarts.

Bonus Features Implemented

Persistent Redis storage using a named Docker volume

## What I Learned

How Docker containers isolate applications and dependencies

Writing Dockerfiles for Python applications

Using Docker Compose to orchestrate multiple containers

Service-to-service communication using Docker networking

Persisting data using Docker volumes

Debugging build context and container startup issues

## Challenges & Solutions

Build context errors – resolved by aligning Docker Compose build paths with the project structure

Container networking – learned to use service names instead of localhost

Dockerfile naming issues – resolved by ensuring correct filename capitalisation

## Notes

This project forms part of my DevOps learning journey and sets the foundation for later modules involving Kubernetes and CI/CD pipelines.

### Additional Learning
- Built and ran Docker images locally
- Used Docker Compose to orchestrate multi-container applications
- Practised image tagging and publishing concepts (Docker Hub)
- Implemented persistent storage using Docker volumes

### Docker Commands Practised

# Build an image from a Dockerfile
docker build -t my-app .

# Run a container locally and map ports
docker run -d -p 5000:5000 my-app

# List running containers
docker ps

# List all containers (including stopped)
docker ps -a

# Inspect container configuration and networking
docker inspect <container_id>

# View container logs
docker logs <container_id>

# Stop and remove containers
docker stop <container_id>
docker rm <container_id>

# Docker Compose commands
docker compose up --build
docker compose down
