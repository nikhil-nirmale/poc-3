FROM python:3.10-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install 

COPY . .

EXPOSE 8080

CMD ["python", "main.py"]
