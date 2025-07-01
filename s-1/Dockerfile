# Use official Python base image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# Copy only requirements first if you have them (for layer caching)
# If no requirements.txt, skip this part or install manually below
# COPY requirements.txt .
# RUN pip install --no-cache-dir -r requirements.txt

# Copy your Python files into the container
COPY main.py .

# ✅ 4. Install dependencies:
# - Flask: your web app framework
# - appdynamics: the Python agent for monitoring
# You're installing the AppDynamics Python agent so it can monitor your app from inside the container.
# When your app starts, it will initialize the agent and send metrics to the AppDynamics controller.
RUN pip install --no-cache-dir Flask pymongo appdynamics    

# Expose the port your app runs on
EXPOSE 8080

# Start the Flask app
CMD ["python", "main.py"]
