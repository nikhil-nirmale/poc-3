# Download the agent
RUN curl -fL -H "Authorization: Bearer <YOUR_TOKEN>" \
  "https://download.appdynamics.com/download/prox/download-file/python/25.6.0.7974/appdynamics-pythonagent-25.6.0.7974-linux-64bit.tar.bz2" \
  -o appd-agent.tar.bz2

# Debug download
RUN file appd-agent.tar.bz2 && ls -l appd-agent.tar.bz2

# Extract agent
RUN tar -xjf appd-agent.tar.bz2

# Debug extraction
RUN ls -R appdynamics-pythonagent-25.6.0.7974

# Cleanup
RUN rm appd-agent.tar.bz2
