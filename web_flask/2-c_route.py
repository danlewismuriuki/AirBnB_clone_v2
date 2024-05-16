#!/usr/bin/python3
"""Flask webApplication"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def Hello_HBNB():
    """Define a route to display 'Hello HBNB"""
    return 'Hello HBNB!'

# # Define a route for the '/hbnb' URL with strict_slashes set to False
@app.route('/hbnb', strict_slashes=False)
def HBNB():
    """Define a route to display 'HBNB"""
    return 'HBNB'

# Define a route for the '/c/<text>' URL with strict_slashes set to False
@app.route('/c/<text>', strict_slashes=False)
def text(text):
    """ Define a route to display 'C' followed by the value of the text variable"""
    text_with_spaces = text.replace('_', ' ')
    # # Return the string 'C ' followed by the modified text_with_spaces as the response
    return 'C {}'.format(text_with_spaces)

# Run the Flask application on host 0.0.0.0 and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
