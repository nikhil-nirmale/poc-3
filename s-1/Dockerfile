FROM python:3.11-slim

WORKDIR /app

# Install required tools
RUN apt-get update && apt-get install -y --no-install-recommends \
    wget bzip2 && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

# Download & extract official AppDynamics Python agent with auth header
RUN wget -O appd-agent.tar.bz2 \
    --header="Authorization: Bearer eyJraWQiOiI1MHV0ZGJVRXRHRWt2dExZVDdOY1FGUkVCaTdOLWptbHBWSzNfM0pOaDZrIiwiYWxnIjoiUlMyNTYifQ.eyJ2ZXIiOjEsImp0aSI6IkFULkRWWjcwYV9oOUxfaEMtNEhkcmdOUWNtUHYyZS1JbUVCWXJoN2ZSWmp4TUUub2FyNG03am9qcmh4bENLdVgycDciLCJpc3MiOiJodHRwczovL2FwcGQtaWRlbnRpdHkub2t0YS5jb20vb2F1dGgyL2F1c3B2bnAzdmtrclNIMk9RMnA2IiwiYXVkIjoibWljb3JzZXJ2aWNlcyIsImlhdCI6MTc1MDc2MTQyOCwiZXhwIjoxNzUwODQ3ODI4LCJjaWQiOiIwb2ExanMxMHQ3ekJjTENnRzJwNyIsInVpZCI6IjAwdTE1M2t0aHVneHJQZmJSMnA4Iiwic2NwIjpbIm9mZmxpbmVfYWNjZXNzIiwiZG93bmxvYWQiLCJvcGVuaWQiXSwiYXV0aF90aW1lIjoxNzUwNzQ3MDE4LCJzdWIiOiJuaWtoaWwubmlybWFsZUA1ZXhjZXB0aW9ucy5jb20ifQ.LFzOvTFhNNxv3Ot6A-7SXZxhTUr-fwD_oHrK1_WCXRkn3fesL8Gaj34NXIS4Jnwvbl8Rgt1MbHtUuBFHDbjRADm2vsa8cJ3byBmI-PZmKL9i6unvFpT0GEhXXqC8draKPWfG-foN8ydpFSHdzigA3QS0KH9lwKgve0Cgg3xn12B2f9wN2XsGrqRyTQx30Uahpg7wxXyaQ8T7RIrb4qJWvnxV32xlMcgw-jOWjdsimU7RQ8sRdmb0qXdu0UGCsxdqZ23qpaTA1JQIOQNj5mjIhjZcowYurD1n_Mou77jVM6Po4guf4QsbuL8jlKxEgWgb2tVcMjEqWu6yc4X5GrfYtQ;" \
    "https://download.appdynamics.com/download/prox/download-file/python/25.6.0.7974/appdynamics-pythonagent-25.6.0.7974-linux-64bit.tar.bz2" && \
    tar -xjf appd-agent.tar.bz2 -C /app && \
    rm appd-agent.tar.bz2

# Copy application source
COPY main.py .

# Install Flask only (no appdynamics pip package)
RUN pip install Flask

# Hardcoded AppDynamics agent config via env vars
ENV APPD_CONTROLLER_HOST=hopper202506172151188.saas.appdynamics.com
ENV APPD_CONTROLLER_PORT=443
ENV APPD_ACCOUNT_NAME=hopper202506172151188
ENV APPD_ACCESS_KEY=sg6s6tdflk8u
ENV APPD_APP_NAME=HelloApp
ENV APPD_TIER_NAME=s-1
ENV APPD_NODE_NAME=Node-s-1
ENV APPD_USE_SSL=true

# Start your app via AppDynamics agent launcher
CMD ["python", "/app/appdynamics-pythonagent-25.6.0.7974/appdynamics-run.py", "main.py"]
