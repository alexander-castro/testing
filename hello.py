"""System module."""
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello_world():
    """A dummy docstring."""
    return "<p>Hello, Next!</p>"
