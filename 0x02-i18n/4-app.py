#!/usr/bin/env python3
"""Sets up basic Flask app."""
from flask import Flask
from flask import request
from flask_babel import _
from flask_babel import Babel
from flask import render_template

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Class to configure available languages."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """Gets the best match from supported languages."""
    locale = request.args.get('locale')
    if locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route("/")
def index():
    """View function for route /."""
    return render_template("4-index.html")


if __name__ == "__main__":
    app.run(debug=True)
