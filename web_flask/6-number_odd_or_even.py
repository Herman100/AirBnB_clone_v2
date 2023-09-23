#!/usr/bin/python3
"""
This module starts a Flask web application
"""

from flask import Flask
from flask import abort, render_template
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


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_default_text(text):
    """
    This function returns the string "Python" followed
    by the value of the text variable
    when the route '/python/<text>' is requested with default 'is cool'
    """
    display = text.replace("_", " ")
    return "Python {}".format(display)


@app.route('/number/<n>', strict_slashes=False)
def interger_text(n):
    """
    This function returns the string "n is a number"
    when the route '/number/<n>' is requested if n is an integer
    """
    if n.isdigit():
        return "{} is a number".format(n)
    else:
        abort(404)


@app.route('/number_template/<n>', strict_slashes=False)
def interger_html(n):
    """
    This function returns an HTML Page
    when the route '/number_template/<n>' is requested if n is an integer
    """
    if n.isdigit():
        return render_template('5-number.html', n=n)
    else:
        abort(404)


@app.route('/number_odd_or_even/<n>', strict_slashes=False)
def interger_even_odd(n):
    """
    This function returns an HTML Page
    when the route '/number_odd_or_even/<n>' is requested if n is an integer
    """
    if n.isdigit():
        outcome = int(n) % 2
        if outcome == 0:
            out = "even"
        else:
            out = "odd"
        return render_template('6-number_odd_or_even.html', n=n, result=out)
    else:
        abort(404)


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
