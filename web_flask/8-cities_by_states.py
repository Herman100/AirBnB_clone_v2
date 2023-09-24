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
    """function to close the database sessions
    """
    storage.close()


@app.route('/cities_by_states', strict_slashes=False)
def list_states():
    """provides a list of all the states to be sorted and rendered
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('8-cities_by_states.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
