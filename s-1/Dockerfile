FROM python:3.11-slim

WORKDIR /app

# 1. Install wget first
RUN apt-get update && apt-get install -y wget tar

# 2. Fixed auth format (Basic instead of Bearer)
RUN wget -O /tmp/appd-py-agent.tar.bz2 \
    --header="Authorization: Basic $(echo -n 'hopper202506172151188:sg6s6tdflk8u' | base64 -w0)" \
    "https://download.appdynamics.com/download/prox/download-file/python/23.7.0.3582/linux-x64" && \
    tar -xjf /tmp/appd-py-agent.tar.bz2 -C /opt/appdynamics && \
    rm /tmp/appd-py-agent.tar.bz2

COPY main.py .
RUN pip install Flask

EXPOSE 8080
CMD ["python", "main.py"]
