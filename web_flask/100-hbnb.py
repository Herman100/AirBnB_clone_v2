#!/usr/bin/python3
"""A flask python script that returns an html page and
renders te hbnb static web page
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


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """
    Provides a list of all the states, cities and amenities
    to be sorted and rendered.
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('100-hbnb.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
