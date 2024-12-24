# syntax=docker/dockerfile:1.2
FROM python:latest
# put you docker configuration here

# Set the working directory in the container
WORKDIR /app

# Copy the requirements.txt file first to leverage Docker cache for dependencies installation
COPY requirements.txt .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the entire project to the container (excluding files listed in .dockerignore)
COPY challenge /app/challenge

# Ensure the model is included in the Docker image
COPY models/model_latest.joblib /app/models/model_latest.joblib

# Install Gunicorn and Uvicorn for running FastAPI
RUN pip install gunicorn uvicorn

# Expose port 8080 for the FastAPI app
EXPOSE 8080

# Define the entry point for the app using Gunicorn with Uvicorn worker for FastAPI
CMD ["gunicorn", "-w", "4", "-k", "uvicorn.workers.UvicornWorker", "challenge.api:app"]
