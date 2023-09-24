#!/usr/bin/python3
"""A flask python script that returns an html page and
contains two defined funtions for route and closing db after each session
"""

from flask import Flask, escape, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception=None):
    """
    Function to close the current database sessions.
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def city_by_states():
    """
    Provides a list of all the states to be sorted and rendered.
    """
    return render_template('8-cities_by_states.html',
                           states=storage.all('State').values())


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
