#!/usr/bin/python3
"""A flask python script that returns an html page and
contains two defined funtions for route and closing db after each session
"""

from flask import Flask, render_template
from models import storage
from models.state import State

app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception=None):
    """
    Function to close the database sessions.
    """
    storage.close()


@app.route('/hbnb_filters', strict_slashes=False)
def hbnb_filters():
    """
    Provides a list of all the states and cities to be sorted and rendered.
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('10-hbnb_filters.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
