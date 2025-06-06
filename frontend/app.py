from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route("/")
def index():
    r = requests.get("http://backend:8000/songs")
    return render_template("index.html", songs=r.json())
