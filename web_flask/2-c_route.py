#!/usr/bin/python3
""" flask script """

from flask import Flask, escape


app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_route():
    """function for web app route"""
    return "Hello HBNB!"

@app.route("/hbnb", strict_slashes=False)
def hello_hbnb():
    """function for hbnb route"""
    return "HBNB"

@app.route("/c/<text>", strict_slashes=False)
def c_route(text):
    """displays value of /c/<text> web app route"""
    text = text.replace("_", " ")
    return "C %s" % text

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
