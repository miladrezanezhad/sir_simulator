# Use official lightweight Python image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Prevent Python from writing .pyc and buffer stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

# Install system dependencies
RUN apt-get update && apt-get install -y --no-install-recommends \
    build-essential \
    curl \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy project source and configuration
COPY . .

# Install project package
RUN pip install --no-cache-dir -e .

# Expose Streamlit default port
EXPOSE 8501

# Healthcheck for container status
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run Streamlit dashboard
ENTRYPOINT ["streamlit", "run", "src/sir_simulator/user_interface/app.py", "--server.port=8501", "--server.address=0.0.0.0"]
