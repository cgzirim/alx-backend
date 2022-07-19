#!/usr/bin/env python3
"""Sets up basic Flask app."""
from flask import Flask
from flask_babel import Babel
from flask import render_template

app = Flask(__name__, template_folder='templates')
babel = Babel(app)


class Config(object):
    """Class to configure available languages."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.form_object(Config)


@app.route("/")
def index():
    """View function for route /."""
    return render_template("1-index.html")


if __name__ == "__main__":
    app.run(debug=True)
