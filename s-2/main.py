# main.py
#  **Controller URL** | https://hopper202506172151188.saas.appdynamics.com
#  **Account Name**   | hopper202506172151188  
#  **Access Key**     | sg6s6tdflk8u  
#  **Use SSL**        | True
#  **Port**           | 443
#  **Service Name**   | s-1

import appdynamics.agent
from flask import Flask
import os

# Initialize AppDynamics agent before app starts
appdynamics.agent.start({
    'controller': 'hopper202506172151188.saas.appdynamics.com',
    'port': 443,
    'ssl': True,
    'account': 'hopper202506172151188',
    'accesskey': 'sg6s6tdflk8u',
    'application': 'HelloApp',
    'tier': 's-1',
    'node': 'Node-s-1'
})

app = Flask(__name__)

@app.route("/")
def home():
    return "✅ Hello from your GitHub Actions demo app! Welcome"

@app.route("/healthz")
def health():
    return "ok"

if __name__ == "__main__":
    port = int(os.environ.get("PORT", 8080))
    print(f"🚀 Starting app on port {port}")
    app.run(host="0.0.0.0", port=port)
