import time
import os
from dotenv import load_dotenv

from daytona import Daytona, CreateSandboxBaseParams

# ✅ Load environment variables
load_dotenv()

# ✅ Initialize Daytona — picks up API key from env vars
daytona = Daytona()

# ✅ Example: just use the official Python image
sandbox = daytona.create(
    CreateSandboxBaseParams(image="python:3.12"),
    on_logs=print,
)

print("Sandbox created using official Python image!")

# Optional: copy files or run commands inside the sandbox
# You might want to upload 'nearest_churches.py' into it using Daytona's file methods.

# Dockerfile
FROM python:3.12

WORKDIR /app
COPY nearest_churches.py .

RUN pip install pandas geopy haversine pillow pygments

CMD ["python", "nearest_churches.py"]

FROM python:3.9

# Install Node.js
RUN curl -fsSL https://deb.nodesource.com/setup_lts.x | bash -
RUN apt-get install -y nodejs

# Verify installations
RUN python --version && node -v && npm -v


# Use an official Python runtime as a parent image
FROM python:3.10-slim

# Set the working directory inside the container
WORKDIR /app

# Install system dependencies for geopy & others
RUN apt-get update && apt-get install -y \
    build-essential \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container at /app
COPY . /app

# Install python dependencies
RUN pip install --no-cache-dir pandas geopy haversine

# Command to run the script when the container starts
CMD ["python", "nearest_churches.py"]