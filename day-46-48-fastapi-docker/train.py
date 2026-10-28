# train.py
import joblib
from app.logger import logger
from xgboost import XGBRegressor
import os

logger.info("Model traing start ho ra hei")

# Dummy Data: [Year, Mileage, Engine_CC]
X_train = [
    [2015, 60000, 1300], 
    [2020, 20000, 1500], 
    [2012, 120000, 1000]
]
# Dummy Target: [Car Prices]
y_train = [2200000, 4500000, 1400000] 

# Model initialize aur train kiya
model = XGBRegressor()
model.fit(X_train, y_train)

# Models ka folder agar nahi hai toh banayega
os.makedirs("models", exist_ok=True)

# Trained dimaagh ko file mein save kar diya
joblib.dump(model, "models/dummy_car_model.pkl")

logger.info("Boom! Model train ho gaya aur 'models/dummy_car_model.pkl' mein save ho gaya.")