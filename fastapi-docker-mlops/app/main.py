from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.logger import logger
from app.config import MODEL_PATH
from fastapi.responses import JSONResponse
from app.schemas import PredictionRequest, PredictionResponse, HealthResponse
from app.ml_model import MLPredictor  # Import the class we created

# Initialize the predictor object globally
predictor = MLPredictor(model_path=MODEL_PATH)

@asynccontextmanager
async def lifespan(app: FastAPI):
    logger.info("Service start ho rahi hai. Model load kiya ja raha hai...")
    # Model loading logic is now encapsulated inside the class
    predictor.load_model()
    yield
    logger.info("Service band ho rahi hai, memory clean kar rahe hain.")
    # Agar model memory release karni ho toh predictor class mein clear method bana sakte hain
    predictor.model = None 

app = FastAPI(title="ML Production API", lifespan=lifespan)
@app.get("/health", response_model=HealthResponse)
async def health_check():
    if predictor.model is None:
        return JSONResponse(
            status_code=503,
            content={
                "status": "not_ready",
                "model_status": "not_loaded"
            }
        )

    if predictor.is_fallback:
        return JSONResponse(
            status_code=503,
            content={
                "status": "not_ready",
                "model_status": "fallback"
            }
        )

    return HealthResponse(
        status="ok",
        model_status="ready"
    )

@app.post("/predict", response_model=PredictionResponse)
async def predict_endpoint(request: PredictionRequest):
    logger.info("Prediction request received")
    
    # Clean inference: FastAPI route doesn't know HOW the prediction happens
    predicted_value = predictor.predict(request.model_dump())
    
    logger.info("Prediction successful!")
    return PredictionResponse(
        prediction=predicted_value,
        probability=0.85, # Isey bhi baad mein class se fetch karenge
        message="API aur ML Model bilkul theek chal rahe hain!"
    )