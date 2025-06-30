# Start from a base image
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy your service code
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Expose the port
EXPOSE 8080

# Run the app
CMD ["python", "main.py"]
