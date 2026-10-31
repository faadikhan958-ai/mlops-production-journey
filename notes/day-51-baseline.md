# Day 51 — Repository Audit + Working Baseline

Date: 31 October 2026

## 1. Repository
- Root: D:\mlops-production-journey
- Main app: day-46-48-fastapi-docker/
- Docker Compose: docker-compose.yml
- Notes: notes/

## 2. Application Structure
- app/main.py: FastAPI application and /predict endpoint
- app/schemas.py: PredictionRequest and PredictionResponse
- app/ml_model.py: ML model loading and prediction class
- app/logger.py: Logging configuration
- models/dummy_car_model.pkl: Serialized model
- Dockerfile: API image instructions
- requirements.txt: Python dependencies
- .dockerignore: Docker build exclusions

## 3. Python Environment
- Activated existing virtual environment.
- Verified Python executable.
- Ran: python -m pip check
- Result: No broken requirements found.

## 4. Local API Test
Command:
python -m uvicorn app.main:app --host 127.0.0.1 --port 8001

Result:
- Server started successfully.
- Model loaded successfully.
- Swagger UI: http://127.0.0.1:8001/docs
- POST /predict returned HTTP 200.
- Shutdown completed successfully.

Test request:
{
  "feature_1": 10.5,
  "feature_2": 20.5,
  "age": 25
}

Test response:
{
  "prediction": 25000,
  "probability": 0.85,
  "message": "API aur ML Model bilkul theek chal rahe hain!"
}

## 5. Docker Compose Verification
Commands executed:
- docker compose config
- docker compose ps
- docker compose build
- docker compose up -d
- docker compose logs api

Results:
- Compose configuration validated.
- API image built successfully.
- API container running on host port 8000.
- model_inference container running.
- Model loaded successfully inside API container.
- POST /predict returned HTTP 200.

## 6. Docker Services
- api: FastAPI application using Python 3.11 slim.
- model_inference: Python 3.9 slim placeholder container.
- Network: mlops-network (bridge).
- API port mapping: 8000:8000.

Note: model_inference currently runs tail -f /dev/null.
It does not perform actual inference.

## 7. Warnings
- Compose version attribute is obsolete; non-fatal.
- XGBoost pickle compatibility warning; model still loaded successfully.

## 8. Important Limitation
MLPredictor currently loads the pickle model,
but predict() returns a hardcoded value of 25000.0.
Probability 0.85 is also hardcoded.

Actual ML inference is not yet implemented or verified.

## 9. Git Status
Modified:
day-46-48-fastapi-docker/.dockerignore

Intentional change:
Removed *.pkl so the model file can be included
in the Docker build context.

Change inspected using git diff.
No commit made.
## 10. Next Tasks
- Implement actual ML model inference.
- Add automated tests using Pytest.
- Review PostgreSQL and SQLAlchemy.
- Continue building production-style AI projects.

## 11. Career Sprint — 31 October 2026

### Job Posts
1. KCloudAI — Internship Program (Lahore, AI/ML track)
   https://www.kcloudai.com/careers/internship-program

2. Vaival Technologies — AI Engineer Intern
   https://www.itjobsinpakistan.com/jobs/view/ai-engineer-intern-2
   Listed deadline: 10 December 2026.
   Note: Listing mentions 2 years experience.

3. BugBrain — AI / LLM Engineer Intern
   https://bugbrain.tech/careers/ai-llm-engineer-intern

### Skill Gap Analysis

Existing strengths:
- Python
- Machine Learning and XGBoost
- FastAPI and REST APIs
- Docker
- Git and GitHub

Skills to strengthen:
- PostgreSQL and SQLAlchemy
- Pytest and automated testing
- RAG and vector databases
- LLM API integration
- AI agents and tool calling
- LLM evaluation and guardrails
- TypeScript (for LLM-focused roles)

### Career Priority
Build demonstrable production-style AI projects and apply
for suitable Lahore internships.## 10. Next Tasks
- Implement actual ML model inference.
- Add automated tests using Pytest.
- Review PostgreSQL and SQLAlchemy.
- Continue building production-style AI projects.
