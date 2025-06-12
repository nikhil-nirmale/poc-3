from flask import Flask
import os

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

