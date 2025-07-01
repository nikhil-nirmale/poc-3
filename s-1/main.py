from flask import Flask
from pymongo import MongoClient

app = Flask(__name__)

# Changed the MongoDB connection string hostname from 'mongo' to 'mongo-container'
client = MongoClient("mongodb://admin:admin123@mongo-container:27017/")

db = client.demo_db
visitors = db.visitors

@app.route("/")
def home():
    # Example: count visitors
    visitors.insert_one({"visited": True})
    count = visitors.count_documents({})
    return f"✅ Flask App Running. Visit count: {count}"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
