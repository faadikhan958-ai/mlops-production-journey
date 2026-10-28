# 1. Python ka chota (slim) version download karo
FROM python:3.11-slim

# 2. Container ke andar ek 'app' naam ka working folder banao
WORKDIR /app

# 3. Apne laptop se sirf requirements.txt copy karo
COPY requirements.txt .

# 4. Saari libraries install karo
RUN pip install --no-cache-dir -r requirements.txt

# 5. Ab apna saara code container mein copy karo
COPY . .

# 6. Container start hote hi FastAPI server chala do
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]