import os
from flask import Flask


app = Flask(__name__)


@app.route("/")
def home():
    return "Hello, this is sample web home page."


@app.route("/hello")
def hello():
    return "Hello, how are you doing?"


if __name__ == "__main__":
    app.run()
