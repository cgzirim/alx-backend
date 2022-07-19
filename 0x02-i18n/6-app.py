#!/usr/bin/env python3
"""Sets up basic Flask app."""
from flask import Flask
from flask import request, g
from flask_babel import Babel
from flask import render_template
from typing import Union

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Class to configure available languages."""

    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[dict, None]:
    "Gets a user."
    login_as = request.args.get("login_as", None)
    if login_as is None:
        return None
    return users.get(int(login_as))


@app.before_request
def before_request():
    """Sets a user as a global on flask.g.user."""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale() -> str:
    """Gets the best match from supported languages."""
    locale = request.args.get("locale")
    if locale in app.config["LANGUAGES"]:
        return locale
    if get_user()['locale'] in app.config['LANGUAGES']:
        return get_user()['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def index():
    """View function for route /."""
    return render_template("6-index.html")


if __name__ == "__main__":
    app.run(debug=True)
