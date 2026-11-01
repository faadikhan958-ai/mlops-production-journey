from pydantic import BaseModel, Field

class PredictionRequest(BaseModel):
    feature_1: float = Field(..., description="Pehla feature (float)")
    feature_2: float = Field(..., description="Dusra feature (float)")
    age: int = Field(..., gt=0, le=120, description="Age 0 se 120 ke darmiyan honi chahiye")

class PredictionResponse(BaseModel):
    prediction: int
    probability: float
    message: str