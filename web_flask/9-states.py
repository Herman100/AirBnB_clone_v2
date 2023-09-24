#!/usr/bin/python3
"""A flask python script that returns an html page
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


@app.route('/states', strict_slashes=False)
def list_states():
    """
    Provides a list of all the states to be sorted and rendered.
    """
    states = storage.all(State).values()
    states = sorted(states, key=lambda state: state.name)
    return render_template('9-states.html', states=states)


@app.route('/states/<id>', strict_slashes=False)
def list_cities(id):
    """
    Provides a list of all the cities in a state to be sorted and rendered.
    """
    states = storage.all(State).values()
    for state in states:
        if state.id == id:
            cities = sorted(state.cities, key=lambda city: city.name)
            return render_template('9-states.html', state=state, cities=cities)
    return render_template('9-states.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
