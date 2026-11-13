from sqlalchemy import URL
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
INFERENCE_SERVICE_URL = os.getenv(
    "INFERENCE_SERVICE_URL",
    "http://model_inference:8001"
)
# PostgreSQL configuration
POSTGRES_HOST = os.getenv("POSTGRES_HOST", "postgres")
POSTGRES_PORT = int(os.getenv("POSTGRES_PORT", "5432"))
POSTGRES_DB = os.getenv("POSTGRES_DB")
POSTGRES_USER = os.getenv("POSTGRES_USER")
POSTGRES_PASSWORD = os.getenv("POSTGRES_PASSWORD")
required_db_settings = {
    "POSTGRES_DB": POSTGRES_DB,
    "POSTGRES_USER": POSTGRES_USER,
    "POSTGRES_PASSWORD": POSTGRES_PASSWORD,
}

missing_settings = [
    name
    for name, value in required_db_settings.items()
    if not value
]

if missing_settings:
    raise ValueError(
        "Missing required database environment variables: "
        + ", ".join(missing_settings)
    )
DATABASE_URL = URL.create(
    drivername="postgresql+psycopg",
    username=POSTGRES_USER,
    password=POSTGRES_PASSWORD,
    host=POSTGRES_HOST,
    port=POSTGRES_PORT,
    database=POSTGRES_DB,
)
