#!/usr/bin/python3
""" Flask web application """

from flask import Flask
from models import storage
from models.state import State

app = Flask(__name__)


@app.route('/states_list', strict_slashes=False)
def list_state():
    """Displays a HTML page with a list of all states"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def tear_down(self):
    """ Closes sqlAlchemy session """
    storage.close()


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
