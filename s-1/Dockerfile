FROM python:3.11-slim

WORKDIR /app

# Install dependencies (no AppDynamics download)
RUN apt-get update && apt-get install -y --no-install-recommends \
    python3-pip && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

COPY main.py .
RUN pip install Flask appdynamics

EXPOSE 8080
CMD ["python", "main.py"]
