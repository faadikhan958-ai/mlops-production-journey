
from contextlib import asynccontextmanager
from fastapi import FastAPI
from uuid import uuid4
import httpx

from app.logger import logger
from app.config import INFERENCE_SERVICE_URL
from fastapi.responses import JSONResponse
from app.schemas import (
    PredictionRequest,
    PredictionResponse,
    HealthResponse
)


@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Main API service starting...")

    app.state.http_client = httpx.AsyncClient(
        base_url=INFERENCE_SERVICE_URL,
        timeout=10.0
    )

    yield

    await app.state.http_client.aclose()

    logger.info("Main API service shutting down...")


app = FastAPI(
    title="ML Production API",
    lifespan=lifespan
)


@app.get("/health", response_model=HealthResponse)
async def health_check():
    try:
        response = await app.state.http_client.get("/health")
        response.raise_for_status()

        return HealthResponse(
            status="ok",
            model_status="ready"
        )

    except httpx.HTTPError:
        return JSONResponse(
            status_code=503,
            content={
                "status": "not_ready",
                "model_status": "unavailable"
            }
        )


@app.post("/predict", response_model=PredictionResponse)
async def predict_endpoint(request: PredictionRequest):

    request_id = str(uuid4())

    logger.info(f"{request_id} | Prediction request received")

    try:
        response = await app.state.http_client.post(
            "/predict",
            json=request.model_dump()
        )

        response.raise_for_status()

        result = response.json()

        prediction = result["prediction"]
        message = result["message"]

        logger.info(f"{request_id} | Prediction successful!")

        return PredictionResponse(
            prediction=prediction,
            probability=0.85,
            message=message
        )

    except httpx.TimeoutException:
        logger.error(f"{request_id} | Inference service timeout")

        return JSONResponse(
            status_code=504,
            content={
                "detail": "Inference service timeout"
            }
        )

    except httpx.ConnectError:
        logger.error(f"{request_id} | Inference service unavailable")

        return JSONResponse(
            status_code=503,
            content={
                "detail": "Inference service unavailable"
            }
        )

    except httpx.HTTPStatusError:
        logger.error(f"{request_id} | Inference service returned HTTP error")

        return JSONResponse(
            status_code=502,
            content={
                "detail": "Inference service returned an error"
            }
        )
