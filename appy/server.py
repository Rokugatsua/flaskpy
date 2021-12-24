from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route("/")
def hello_world():
    return "<h1> Hello World </h1>"


@app.route("/hello")
def hello():
    return f"Hello, "


@app.route("/u/<string:name>")
def user(name):
    return f"Hello user, {escape(name)}"


@app.route("/login")
def login():
    return "login page"