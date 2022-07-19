#!/usr/bin/env python3
"""Sets up basic Flask app."""
from flask import Flask
from flask import render_template

app = Flask(__name__)


@app.route("/", strick_slashes=False)
def index():
    """View function for route /."""
    return render_template("0-index.html")
