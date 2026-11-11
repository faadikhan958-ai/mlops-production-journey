from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Model Inference Service")


class PredictionRequest(BaseModel):
    feature_1: float
    feature_2: float
    age: int


class PredictionResponse(BaseModel):
    prediction: float
    message: str


@app.get("/health")
def health():
    return {"status": "ok"}


@app.post("/predict", response_model=PredictionResponse)
def predict(request: PredictionRequest):
    prediction = 25000.0

    return PredictionResponse(
        prediction=prediction,
        message="Prediction generated successfully"
    )