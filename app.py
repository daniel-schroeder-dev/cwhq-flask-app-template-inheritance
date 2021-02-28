from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.jinja")

@app.route("/login")
def login():
    return render_template("login.jinja")

@app.route("/signup")
def signup():
    return render_template("signup.jinja")
