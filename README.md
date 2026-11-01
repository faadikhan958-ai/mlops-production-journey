# My 90 Days MLOps & Production AI Journey

A hands-on journey toward building production-ready AI/ML systems using Python, FastAPI, Docker, and MLOps practices.

## Project Overview

This repository contains a containerized Machine Learning API built with FastAPI and Docker Compose.

### Services

| Service | Purpose |
|---|---|
| `api` | FastAPI application serving ML predictions |
| `model_inference` | Python container reserved for ML inference experiments |
| `mlops-network` | Bridge network connecting the services |

## Tech Stack

- Python 3.11
- FastAPI
- Pydantic
- Uvicorn
- XGBoost
- Scikit-learn
- Joblib
- Docker
- Docker Compose

## Project Structure

```text
mlops-production-journey/
├── fastapi-docker-mlops/
│   ├── app/
│   │   ├── main.py
│   │   ├── ml_model.py
│   │   ├── schemas.py
│   │   └── logger.py
│   ├── models/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .dockerignore
├── notes/
├── docker-compose.yml
└── README.md
```

## Prerequisites

- Docker Desktop installed and running
- Git installed

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/faadikhan958-ai/mlops-production-journey.git
cd mlops-production-journey
```

### 2. Build the API image

```bash
docker compose build api
```

### 3. Start the services

```bash
docker compose up -d
```

### 4. Check running containers

```bash
docker compose ps
```

### 5. Open the API documentation

Visit:

http://localhost:8000/docs

Use the interactive Swagger UI to test the prediction endpoint.

## Useful Docker Commands

View API logs:

```bash
docker compose logs api
```

Follow API logs:

```bash
docker compose logs -f api
```

Stop and remove the Compose containers and network:

```bash
docker compose down
```

Rebuild the API image after code or dependency changes:

```bash
docker compose build api
docker compose up -d
```

## Docker Build Practices

This project follows several useful Docker practices:

- Dependency installation is performed before copying application source code to improve layer caching.
- `.dockerignore` excludes unnecessary files from the Docker build context.
- Virtual environments, Git metadata, environment files, and Python cache files are excluded from the image build context.
- Dependency versions are pinned in `requirements.txt`.
- The application listens on `0.0.0.0:8000` inside the container.

## Learning Progress

This repository is part of a structured 90-day AI/ML and MLOps learning journey, focused on practical implementation and production-oriented engineering.

More project notes and milestones are maintained in the `notes/` directory.