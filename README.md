# My 90 Days MLOps & Production AI Journey

A hands-on journey toward building production-ready AI/ML systems using Python, FastAPI, Docker, Docker Compose, and MLOps practices.

## Project Overview

This repository contains a containerized Machine Learning API built with FastAPI and Docker Compose.

The application uses a **separated service architecture**, where the Main API handles incoming requests and communicates with a dedicated Model Inference API over an internal Docker network.

The project focuses on production-oriented engineering practices, including service communication, request validation, logging, error handling, containerization, and integration testing.

## System Architecture

```text
              User / Client
                    |
                    v
          Main API (FastAPI)
              Port 8000
                    |
                    | HTTP Request
                    | HTTPX AsyncClient
                    v
       Model Inference API (FastAPI)
              Port 8001
                    |
                    v
          Prediction Response
                    |
                    v
              Main API
                    |
                    v
              User / Client
```

Both services communicate through the internal Docker Compose network named `mlops-network`.

## Services

| Service | Purpose |
|---|---|
| `api` | Main FastAPI application that receives requests, validates input, and forwards prediction requests |
| `model_inference` | Separate FastAPI service responsible for prediction processing |
| `mlops-network` | Docker bridge network connecting both services |

## Tech Stack

- Python 3.11
- FastAPI
- Pydantic
- Uvicorn
- HTTPX
- Scikit-learn
- XGBoost
- Joblib
- Docker
- Docker Compose

## Project Structure

```text
mlops-production-journey/
│
├── fastapi-docker-mlops/
│   ├── app/
│   │   ├── main.py
│   │   ├── ml_model.py
│   │   ├── schemas.py
│   │   ├── logger.py
│   │   └── config.py
│   │
│   ├── models/
│   ├── Dockerfile
│   ├── requirements.txt
│   └── .dockerignore
│
├── model-inference/
│   ├── app/
│   │   └── main.py
│   ├── Dockerfile
│   └── requirements.txt
│
├── notes/
├── docker-compose.yml
└── README.md
```

## Prerequisites

- Python 3.11
- Docker Desktop installed and running
- Git installed

## Getting Started

### 1. Clone the repository

```bash
git clone https://github.com/faadikhan958-ai/mlops-production-journey.git

cd mlops-production-journey
```

### 2. Build both service images

```bash
docker compose build
```

### 3. Start both services

```bash
docker compose up -d
```

### 4. Check running containers

```bash
docker compose ps
```

Both services should be running.

### 5. Access API documentation

Main API Swagger documentation:

http://localhost:8000/docs

Model Inference API Swagger documentation:

http://localhost:8001/docs

Use the interactive Swagger UI to test the endpoints.

## API Endpoints

### Main API — Port 8000

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Checks the availability of the inference service |
| POST | `/predict` | Receives prediction requests and forwards them to the inference service |

### Model Inference API — Port 8001

| Method | Endpoint | Purpose |
|---|---|---|
| GET | `/health` | Returns inference service health status |
| POST | `/predict` | Processes prediction requests |

## Prediction Request

Example request for `POST /predict`:

```json
{
    "feature_1": 10.5,
    "feature_2": 20.5,
    "age": 25
}
```

### Successful Response

```json
{
    "prediction": 25000,
    "probability": 0.85,
    "message": "Prediction generated successfully"
}
```

**Note:** The current inference implementation uses a placeholder prediction value (`25000.0`), and the probability (`0.85`) is also hardcoded in the Main API. These are demonstration values, not actual trained-model predictions.

## Error Handling

The Main API handles common communication errors when interacting with the Model Inference API.

| HTTP Status | Error | Description |
|---|---|---|
| 503 | Service Unavailable | Inference service connection could not be established |
| 504 | Gateway Timeout | Inference service did not respond within the configured timeout |
| 502 | Bad Gateway | Inference service returned an unsuccessful HTTP status |

### Timeout Configuration

The HTTPX client uses a 10-second timeout.

```python
app.state.http_client = httpx.AsyncClient(
    base_url=INFERENCE_SERVICE_URL,
    timeout=10.0
)
```

### Error Handling Implementation

```python
except httpx.TimeoutException:
    return JSONResponse(
        status_code=504,
        content={"detail": "Inference service timeout"}
    )

except httpx.ConnectError:
    return JSONResponse(
        status_code=503,
        content={"detail": "Inference service unavailable"}
    )

except httpx.HTTPStatusError:
    return JSONResponse(
        status_code=502,
        content={"detail": "Inference service returned an error"}
    )
```

## Useful Docker Commands

### View API logs

```bash
docker compose logs api
```

### View inference service logs

```bash
docker compose logs model_inference
```

### Follow API logs

```bash
docker compose logs -f api
```

### Follow inference service logs

```bash
docker compose logs -f model_inference
```

### Stop services

```bash
docker compose stop
```

### Start services

```bash
docker compose start
```

### Stop and remove containers and network

```bash
docker compose down
```

### Rebuild and restart services

```bash
docker compose up --build -d
```

## Docker Build Practices

This project follows several useful Docker practices:

- Dependency installation is performed before copying application source code to improve layer caching.
- `.dockerignore` excludes unnecessary files from the Docker build context.
- Virtual environments, Git metadata, environment files, and Python cache files are excluded from the image build context.
- Dependency versions are pinned in `requirements.txt`.
- Both services run in separate containers.
- Docker Compose provides internal networking between services.
- Applications listen on `0.0.0.0` inside their respective containers.

## Integration Testing

The following scenarios have been tested:

- Both Docker containers start successfully.
- Main API health check returns `200 OK`.
- Main API successfully communicates with Model Inference API.
- End-to-end prediction request returns `200 OK`.
- Stopping the inference service triggers connection error handling (`503`).
- Delayed inference response triggers timeout handling (`504`).
- Upstream HTTP errors are handled using `502`.

## Learning Progress

This repository is part of a structured 90-day AI/ML and MLOps learning journey, focused on practical implementation and production-oriented engineering.

The learning journey includes:

- Python and Machine Learning fundamentals
- Model development and evaluation
- FastAPI model serving
- Docker containerization
- Logging inside containers
- Separate inference service architecture
- Asynchronous HTTP communication
- Timeout and connection error handling
- End-to-end integration testing
- Production-oriented documentation

More project notes and milestones are maintained in the `notes/` directory.

## Repository

GitHub: https://github.com/faadikhan958-ai/mlops-production-journey