
import pickle
import logging
from pathlib import Path

logger = logging.getLogger("ml_api")


class MLPredictor:
    def __init__(self, model_path: str = "models/dummy_car_model.pkl"):
        self.model_path = Path(model_path)
        self.model = None
        self.is_fallback = False

    def load_model(self):
        """Load the ML model from disk into memory."""
        logger.info(f"Loading ML model from {self.model_path}...")

        # Reset previous state before every loading attempt.
        self.model = None
        self.is_fallback = False

        if not self.model_path.exists():
            logger.warning(
                f"Model file {self.model_path} not found. "
                "Loading fallback Dummy Model."
            )
            self.model = "Dummy_Fallback_Model"
            self.is_fallback = True
            return

        try:
            with open(self.model_path, "rb") as file:
                self.model = pickle.load(file)

            logger.info("Model loaded into memory successfully.")

        except Exception:
            logger.exception("Failed to load ML model.")
            self.model = None
            self.is_fallback = False
            raise

    def predict(self, input_data: dict) -> float:
        """Generate a prediction using the loaded model."""

        if self.model is None:
            logger.error("Prediction attempted but model is not loaded.")
            raise ValueError("Call load_model() before predicting.")

        logger.info(f"Running preprocessing and prediction for: {input_data}")

        # Actual production preprocessing and inference will go here.
        # features = preprocess(input_data)
        # return float(self.model.predict([features])[0])

        # Temporary dummy prediction for testing.
        dummy_prediction = 25000.0
        return dummy_prediction
