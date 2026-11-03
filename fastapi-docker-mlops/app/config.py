
import os

MODEL_PATH = os.getenv(
    "MODEL_PATH",
    "models/dummy_car_model.pkl"
)

try:
    API_PORT = int(os.getenv("API_PORT", "8000"))
except ValueError as exc:
    raise ValueError(
        "Invalid API_PORT: please provide a valid integer port."
    ) from exc

if not 1 <= API_PORT <= 65535:
    raise ValueError(
        "Invalid API_PORT: port must be between 1 and 65535."
    )
