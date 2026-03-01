# Use official Python image
FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements first (better Docker caching)
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy all project files
COPY . .

# Expose FastAPI port
EXPOSE 8000

# Start FastAPI using uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]

# DOCKER  TOKEN - dckr_pat_AxaT6sOfsO6jTkF7O5UcBrLT5rQ
#to run the docker --docker run -p 8000:8000 kiki1404/dscapstone-app
