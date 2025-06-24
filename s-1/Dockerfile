FROM python:3.11-slim

WORKDIR /app

# Install dependencies + download agent
RUN apt-get update && \
    apt-get install -y wget tar && \
    wget -O /tmp/appd-py-agent.tar.bz2 \
    "https://download.appdynamics.com/download/prox/download-file/python/23.7.0.3582/linux-x64" && \
    tar -xjf /tmp/appd-py-agent.tar.bz2 -C /opt/appdynamics && \
    rm /tmp/appd-py-agent.tar.bz2 && \
    apt-get clean

COPY main.py .
RUN pip install Flask

EXPOSE 8080
CMD ["python", "main.py"]
