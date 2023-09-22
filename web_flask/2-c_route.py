#!/usr/bin/python3
"""
This module starts a Flask web application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """
    This function returns the string "Hello HBNB!"
    when the route '/' is requested
    """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    This function returns the string "HBNB"
    when the route '/hbnb' is requested
    """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_text(text):
    """
    This function returns the string "C" followed
    by the value of the text variable
    when the route '/c/<text>' is requested
    """
    display = text.replace("_", " ")
    return "C {}".format(display)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
