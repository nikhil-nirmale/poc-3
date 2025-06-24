from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ AppDynamics Monitored App (using official Python Agent)"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
