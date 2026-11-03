# Day 54 — Configuration & Environment Management

## Goal
Separate application configuration from source code using environment variables.

## Implementation

- Created `app/config.py`.
- Configured MODEL_PATH using os.getenv().
- Configured API_PORT using os.getenv().
- Added API_PORT integer and range validation.
- Updated main.py to load MODEL_PATH from config.
- Updated Dockerfile to use API_PORT.
- Updated docker-compose.yml with HOST_PORT, API_PORT and MODEL_PATH.
- Created root .env.example.
- Updated root .gitignore to protect secrets and local databases.
- Updated app .gitignore.

## Testing

- Tested default configuration.
- Tested API_PORT override.
- Tested invalid API_PORT handling.
- Tested MODEL_PATH override.
- Successfully built Docker image.
- Started both Docker Compose services.
- Verified API documentation at /docs.
- Successfully tested POST /predict.

## Docker Configuration

- API container port: 8000
- Host port: 8000
- API service: Running
- Model inference service: Running
- Docker storage moved to D: drive.

## Key Learning

Environment variables allow configuration to change without modifying application source code.

.env stores local configuration, while .env.example provides a safe template.

## Status

Technical implementation and API verification completed.