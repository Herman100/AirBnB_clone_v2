#!/usr/bin/python3
"""A flask python script that returns an html page
"""

from flask import Flask, escape, render_template
from models import storage
from models.state import State
app = Flask(__name__)


@app.teardown_appcontext
def close_db(exception=None):
    """
    Function to close the database sessions.
    """
    storage.close()


@app.route('/states', defaults={'state_id': 'None'}, strict_slashes=False)
@app.route('/states/<path:state_id>', strict_slashes=False)
def states(id_for_state):
    """
    Provides a list of all the states to be sorted and rendered.
    If an id is provided, it provides list of all the cities in that state.
    """
    states = storage.all('State').values()
    for state in states:
        if escape(id_for_state) == state.id:
            return render_template('9-states.html',
                                   states=state, name=state.name)
    return render_template('9-states.html', states=states, name=id_for_state)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
