# Day 57 — Logging Inside Containers
 
**Project:** MLOps Production Journey

## 1. Objective

Learn how to configure, manage, and monitor application logs inside Docker containers.

## 2. Existing Logging Inspection

Inspected the existing logging implementation in:

- `app/logger.py`
- `app/main.py`
- `app/ml_model.py`

Learned:
- How Python logging works.
- Why logging is better than using print().
- How a named logger is shared between modules.
- How logging handlers and formatters work.

## 3. Python Logging Levels

| Level | Purpose |
|---|---|
| DEBUG | Detailed debugging information |
| INFO | Normal application events |
| WARNING | Unexpected situations |
| ERROR | Application errors |
| CRITICAL | Serious failures |

Configured the logger with INFO as the minimum logging level.

## 4. Centralized Logging Configuration

Kept logging configuration in `app/logger.py`.

Important implementation:

- Used `logging.getLogger("ml_api")`.
- Configured the logger level.
- Added a formatter for timestamp, level, and message.
- Used `if not logger.handlers` to prevent duplicate handlers.

**Verification:** Called `setup_logger()` again inside the API container and confirmed that only one handler was registered at that stage.

## 5. stdout and stderr Configuration

Configured two separate logging streams.

- stdout: INFO and WARNING messages.
- stderr: ERROR and CRITICAL messages.

Used separate `StreamHandler` objects for both streams.

**Testing command:**

```powershell
docker compose exec -T api python -c "from app.logger import logger; logger.info('STDOUT TEST'); logger.error('STDERR TEST')" 1> stdout.txt 2> stderr.txt
```

Verified that normal and error messages were redirected to separate files.

## 6. Secure Logging

Reviewed application logs to avoid exposing sensitive information.

Updated `main.py`:

```python
logger.info("Prediction request received")
```

Updated `ml_model.py`:

```python
logger.info("Running preprocessing and prediction")
```

Removed full request data from application log messages.

**Security rule:** Never log passwords, API keys, access tokens, or sensitive personal information.

## 7. API Request and Error Logging

Tested a valid prediction request.

```powershell
Invoke-RestMethod -Uri "http://localhost:8000/predict" -Method POST -ContentType "application/json" -Body '{"feature_1":10.5,"feature_2":20.5,"age":25}'
```

Result:

- Prediction: 25000
- Probability: 0.85
- HTTP Status: 200 OK

Note: The prediction value is currently a dummy test value.

### Invalid Request Testing

Tested an invalid age value of 0.

The API returned:

`422 Unprocessable Entity`

FastAPI rejected the invalid input through Pydantic validation before executing the endpoint function.

## 8. Exception Logging

Learned the difference between:

**logger.error():**
Records an error message.

**logger.exception():**
Records an error message along with traceback information. Normally used inside an except block.

**raise:**
Re-raises the original exception so calling code can handle it.

Example:

```python
try:
    result = 10 / 0
except Exception:
    logger.exception("Calculation failed")
    raise
```

## 9. Docker Logging Commands

Commands practiced:

```powershell
docker compose ps
docker compose logs api
docker compose logs --tail=20 api
docker compose up -d --build api
```

Learned how to inspect container status, view application logs, and rebuild the API container.

## 10. Career and Interview Preparation

Practiced these interview topics:

1. Difference between print() and logging.
2. Python logging levels.
3. Difference between stdout and stderr.
4. Purpose of logger.exception().
5. Meaning of traceback.
6. Purpose of raise.
7. Docker container log inspection.
8. Secure logging practices.
## Additional Verification — 10 November 2026

### 1. Request ID Verification
- Generated a unique UUID for each prediction request.
- Confirmed the same Request ID appears in both request-received and prediction-success logs.
- Verified module names (`main` and `ml_model`) in logs.

### 2. Live Docker Logs
- Verified live logs using `docker compose logs -f api`.
- Confirmed new logs appear while the container is running.
- Stopped live log streaming using `Ctrl + C`.

### 3. Docker Health Check
- Verified container status using `docker compose ps`.
- API status: `Up (healthy)`.
- Health check endpoint: `/health`.
- Interval: 30 seconds.
- Timeout: 5 seconds.
- Retries: 3.
- Start period: 10 seconds.
- Confirmed repeated health-check requests are normal monitoring activity.

### 4. API Prediction Test
- Sent a valid POST request to `/predict`.
- Prediction returned: `25000`.
- Probability returned: `0.85`.
- API response was successful (`200 OK`).

### 5. Exception Logging
- Tested `logger.exception()` inside an `except` block.
- Verified that the error message and traceback were logged.

### 6. Key Learning
- Request IDs help connect logs belonging to the same request.
- Docker health checks monitor application health, not prediction accuracy.
- `logger.exception()` records exception details and traceback.
- Sensitive request payloads should not be logged.

**Status:** Additional verification completed locally. No new Git commit or push performed.

## Day 57 — Completion Checklist

- [x] Inspected existing logging.
- [x] Learned Python logging levels.
- [x] Configured centralized logging.
- [x] Prevented duplicate handlers.
- [x] Configured stdout and stderr.
- [x] Tested separate output streams.
- [x] Removed sensitive request data from logs.
- [x] Tested successful API requests.
- [x] Tested invalid API requests.
- [x] Practiced exception logging and traceback.
- [x] Completed interview practice.
- [ ] Save notes in the project repository.
- [ ] Final Git commit and GitHub push.

**Final Learning:** Implemented and tested Python application logging inside Docker containers using FastAPI, including separate stdout/stderr streams, secure logging practices, and API request/error monitoring.