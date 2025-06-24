from flask import Flask
import appdynamics
import os

# Hardcoded AppDynamics config
appdynamics.agent.init(
    controller='hopper202506172151188.saas.appdynamics.com',
    port=443,
    ssl=True,
    account='hopper202506172151188',
    access_key='sg6s6tdflk8u',
    application='HelloApp',
    tier='s-1',
    node='Node-s-1'
)

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ AppDynamics-Monitored App (Simple Setup)"

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
