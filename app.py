from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route("/")
def top():
    return render_template("top.html")

app.run(host="0.0.0.0", port=5001)