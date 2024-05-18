"""Flask web applicaton"""
from flask import Flask
app = Flask(__name__)


@app.route("/", strict_slashes=False)
def hello_world():
    """Route to display 'Hello HBNB!'."""
    return "Hello HBNB!"

# Run the Flask application on host 0.0.0.0 and port 5000
if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
