#!/usr/bin/python3
"""Start a Flask webapplication"""


from flask import Flask

# create a Flask application instance
app = Flask(__name__)

# define a route for the root URL('/')
@app.route('/', strict_slashes=False)
def hello_hbnb():
    """Define a route to display 'Hello HBNB'"""
    return 'Hello HBNB!'

# Define a route for the '/hbnb' URL
@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ Define a route to display 'HBNB'"""
    return 'HBNB'

# Run the Flask application on host 0.0.0.0 and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
