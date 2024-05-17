from flask import Flask
"""Flask web applicaton"""
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Route to display 'Hello HBNB!'."""
    return "Hello HBNB!"


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
