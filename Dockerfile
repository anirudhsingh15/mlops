# 1. Base Image (We use 3.11 to be modern and stable)
FROM python:3.11-slim

# 2. Work Directory
WORKDIR /app

# 3. Install Dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# 4. Copy Code
COPY . .

# 5. Command to Run
CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]
