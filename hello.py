"""System module."""
from flask import Flask

app = Flasc(__name__)

@app.route("/")
def hello_world():
    """A dummy docstring."""
    return "<p>Hello, Next 2022!</p>"
