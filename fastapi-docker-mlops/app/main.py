from contextlib import asynccontextmanager
from fastapi import FastAPI
from app.logger import logger
from app.schemas import PredictionRequest, PredictionResponse
from app.ml_model import MLPredictor  # Import the class we created

# Initialize the predictor object globally
predictor = MLPredictor(model_path="models/dummy_car_model.pkl")

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

@app.post("/predict", response_model=PredictionResponse)
async def predict_endpoint(request: PredictionRequest):
    logger.info(f"Naya request aaya: {request.model_dump()}")
    
    # Clean inference: FastAPI route doesn't know HOW the prediction happens
    predicted_value = predictor.predict(request.model_dump())
    
    logger.info("Prediction successful!")
    return PredictionResponse(
        prediction=predicted_value,
        probability=0.85, # Isey bhi baad mein class se fetch karenge
        message="API aur ML Model bilkul theek chal rahe hain!"
    )