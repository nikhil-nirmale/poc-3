FROM python:3.11-slim

WORKDIR /app

# Install dependencies + download official Python agent
RUN apt-get update && \
    apt-get install -y wget tar && \
    wget -O /tmp/appd-py-agent.tar.bz2 \
    "https://download.appdynamics.com/download/prox/download-file/python/latest/linux-x64" && \
    tar -xjf /tmp/appd-py-agent.tar.bz2 -C /opt/appdynamics && \
    rm /tmp/appd-py-agent.tar.bz2 && \
    apt-get clean

COPY main.py .
RUN pip install Flask appdynamics

# Set required environment variables
ENV APPDYNAMICS_CONTROLLER_HOST_NAME="hopper202506172151188.saas.appdynamics.com"
ENV APPDYNAMICS_CONTROLLER_PORT="443"
ENV APPDYNAMICS_CONTROLLER_SSL_ENABLED="true"
ENV APPDYNAMICS_AGENT_ACCOUNT_NAME="hopper202506172151188"
ENV APPDYNAMICS_AGENT_ACCOUNT_ACCESS_KEY="sg6s6tdflk8u"
ENV APPDYNAMICS_AGENT_APPLICATION_NAME="HelloApp"
ENV APPDYNAMICS_AGENT_TIER_NAME="s-1"
ENV APPDYNAMICS_AGENT_NODE_NAME="Node-s-1"

EXPOSE 8080
CMD ["python", "main.py"]
