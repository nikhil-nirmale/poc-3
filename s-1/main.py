from flask import Flask, request, render_template_string
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection (works with your running mongo container)
client = MongoClient("mongodb://admin:admin123@mongo-container:27017/")
db = client.demo_db
visitors = db.visitors

# HTML with styling for the welcome message and form
form_html = '''
<!doctype html>
<html>
  <head>
    <title>5X Portal</title>
    <style>
      .welcome {
        font-size: 2em;
        font-weight: bold;
        color: #ffffff;
        background: linear-gradient(90deg, #ff4b1f, #1fddff);
        padding: 20px;
        border-radius: 10px;
        text-align: center;
        box-shadow: 0 4px 8px rgba(0,0,0,0.2);
        margin-bottom: 30px;
      }
    </style>
  </head>
  <body style="font-family: Arial, sans-serif; background-color: #f4f4f4; padding: 40px;">
    <div class="welcome">👋 Welcome to 5X Portal</div>
    <form method="POST">
      <label>Your Name:</label> <input type="text" name="name" required><br><br>
      <label>Your Age:</label> <input type="number" name="age" required><br><br>
      <input type="submit" value="Submit">
    </form>
    {% if message %}
      <p><strong>{{ message }}</strong></p>
    {% endif %}
  </body>
</html>
'''

@app.route("/", methods=["GET", "POST"])
def home():
    message = ""
    if request.method == "POST":
        name = request.form.get("name")
        age = request.form.get("age")
        if name and age:
            visitors.insert_one({"name": name, "age": age})
            message = f"✅ Thank you, {name}. Your details have been saved!"
    return render_template_string(form_html, message=message)

@app.route("/health")
def health():
    return "OK", 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)

#G
