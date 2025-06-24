from flask import Flask
import os
import appdynamics

# Initialize AppDynamics (auto-configures from environment variables)
appdynamics.agent.init()

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ AppDynamics-Monitored Flask App Running!"

@app.route("/healthz")
def health():
    return "HEALTHY", 200

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    app.run(host="0.0.0.0", port=port)
