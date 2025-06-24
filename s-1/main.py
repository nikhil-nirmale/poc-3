from flask import Flask
import os
import appdynamics

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Hello from your GitHub Actions demo app with AppDynamics!"

@app.route("/healthz")
def health():
    return "ok"

if __name__ == "__main__":
    # Agent auto-configures from environment variables
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
