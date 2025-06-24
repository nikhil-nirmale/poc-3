FROM python:3.11-slim

WORKDIR /app

# Install required tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    curl bzip2 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Download and extract AppDynamics agent using curl
RUN curl -fL -H "Authorization: Bearer eyJraWQiOi..." \
    "https://download.appdynamics.com/download/prox/download-file/python/25.6.0.7974/appdynamics-pythonagent-25.6.0.7974-linux-64bit.tar.bz2" \
    -o appd-agent.tar.bz2 && \
    tar -xjf appd-agent.tar.bz2 && \
    test -f appdynamics-pythonagent-25.6.0.7974/appdynamics-run.py && \
    rm appd-agent.tar.bz2

# Copy application
COPY main.py .

# Install dependencies
RUN pip install Flask

# AppDynamics environment variables
ENV APPD_CONTROLLER_HOST=hopper202506172151188.saas.appdynamics.com \
    APPD_CONTROLLER_PORT=443 \
    APPD_ACCOUNT_NAME=hopper202506172151188 \
    APPD_ACCESS_KEY=sg6s6tdflk8u \
    APPD_APP_NAME=HelloApp \
    APPD_TIER_NAME=s-1 \
    APPD_NODE_NAME=Node-s-1 \
    APPD_USE_SSL=true

# Start app via AppDynamics agent launcher
CMD ["python", "/app/appdynamics-pythonagent-25.6.0.7974/appdynamics-run.py", "main.py"]
