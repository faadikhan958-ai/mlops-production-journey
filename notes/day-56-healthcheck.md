# Day 56 — Health Endpoint & Docker Healthcheck

**Date:** 7 November 2026
**Project:** MLOps Production Journey
**Status:** Completed

## 1. Objective

Implement an application readiness endpoint in FastAPI and configure Docker Compose healthchecks to monitor whether the ML API is ready to serve predictions.

A running container does not necessarily mean that its application or ML model is ready.

## 2. Liveness vs Readiness

### Liveness

Checks whether an application process is alive and running.

### Readiness

Checks whether an application is ready to handle requests.

**Project implementation:** The `/health` endpoint acts as a readiness check because it verifies the ML model's loading state.

## 3. FastAPI Health Endpoint

**Route:** `GET /health`

The endpoint checks two predictor properties:

- `predictor.model`: whether a model is loaded.
- `predictor.is_fallback`: whether the active model is a fallback model.

### Healthy response

HTTP Status: `200 OK`

```json
{
  "status": "ok",
  "model_status": "ready"
}
```

### Model not loaded

HTTP Status: `503 Service Unavailable`

```json
{
  "status": "not_ready",
  "model_status": "not_loaded"
}
```

### Fallback model active

HTTP Status: `503 Service Unavailable`

```json
{
  "status": "not_ready",
  "model_status": "fallback"
}
```

`JSONResponse` is used to explicitly return HTTP 503 for unsuccessful readiness checks. `HealthResponse` defines the response structure using Pydantic.

## 4. ML Predictor State Management

Updated `app/ml_model.py`:

- Added `is_fallback` state.
- Reset model state before every loading attempt.
- Set `is_fallback = True` when the real model file is missing and the dummy fallback is loaded.
- Reset state and re-raise the exception if model loading fails.
- A successfully loaded real model remains non-fallback.

This allows the health endpoint to distinguish a real model from a fallback model.

## 5. Docker Compose Healthcheck

Added a healthcheck under the `api` service in the root `docker-compose.yml`.

### Configuration

| Setting | Value | Purpose |
|---|---|---|
| `test` | Python urllib request to `/health` | Runs the readiness check |
| `interval` | `30s` | Time between checks |
| `timeout` | `5s` | Maximum execution time |
| `retries` | `3` | Consecutive failures before unhealthy |
| `start_period` | `10s` | Startup grace period |

The healthcheck sends a request to:

`http://127.0.0.1:8000/health`

It runs inside the API container, so localhost refers to that container.

A successful HTTP response produces a successful healthcheck. An HTTP 503 causes the Python request to fail, resulting in a non-zero command exit code.

The Python request timeout of 2 seconds and Docker healthcheck timeout of 5 seconds are separate timeout settings.

## 6. Testing and Verification

The following checks were performed:

- FastAPI `/health` healthy response verified.
- Missing-model fallback response verified with HTTP 503.
- Existing `/predict` endpoint regression tested.
- Docker Compose healthcheck configured.
- Docker container health status tested.
- Healthy → Unhealthy → Healthy failure experiment completed.
- Main Compose configuration validated.
- Test Compose configuration validated.
- `git diff --check` passed before staging.

### Compose validation commands

```powershell
docker compose config --quiet

docker compose -f docker-compose.test.yml config --quiet
```

Both commands completed without errors.

### Docker rebuild command

```powershell
docker compose up -d --build --no-deps api
```

API image rebuilt and container started successfully.

### Fallback response

```json
{
  "status": "not_ready",
  "model_status": "fallback"
}
```

HTTP status: `503 Service Unavailable`.

## 7. Files Changed

| File | Change |
|---|---|
| `docker-compose.yml` | Added API healthcheck |
| `fastapi-docker-mlops/app/main.py` | Added GET `/health` endpoint |
| `fastapi-docker-mlops/app/ml_model.py` | Added fallback state management |
| `fastapi-docker-mlops/app/schemas.py` | Added `HealthResponse` |
| `docker-compose.test.yml` | Added isolated test Compose configuration |
| `notes/day-56-healthcheck.md` | Documented implementation and verification |

## 8. Key Learnings

- Running and healthy are different container states.
- Readiness checks verify whether an application can serve requests.
- HTTP 200 indicates successful readiness in this project.
- HTTP 503 indicates the service is not ready.
- Docker Compose healthchecks monitor application health, not merely process existence.
- A fallback model should not be reported as a successfully loaded production model.
- Configuration validation should happen before committing changes.

## 9. Git

Planned Conventional Commit:

`feat(api): add health endpoint and container healthcheck`

## 10. Final Outcome

Implemented and verified a FastAPI readiness endpoint and Docker Compose healthcheck for the ML inference service.

The API can distinguish between a successfully loaded real model, a missing model, and an active fallback model.
