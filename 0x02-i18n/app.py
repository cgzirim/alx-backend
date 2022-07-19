#!/usr/bin/env python3
"""Sets up basic Flask app."""
from flask import Flask
from flask import request, g
from flask_babel import Babel
from flask import render_template
from typing import Union
from datetime import datetime
from pytz import UnknownTimeZoneError, timezone

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

    if g.user:
        locale = g.user.get("locale")
        if locale and locale in app.config["LANGUAGES"]:
            return locale

    return request.accept_languages.best_match(app.config["LANGUAGES"])


@babel.timezoneselector
def get_timezone():
    """Infer appropraite time zone."""
    try:
        if request.args.get("timezone"):
            time_zone = timezone(request.args.get("timezone"))
        else:
            if g.user and g.user.get("timezone"):
                time_zone = timezone(g.user.get("timezone"))
    except UnknownTimeZoneError:
        time_zone = app.config["BABEL_DEFAULT_TIMEZONE"]

    return time_zone


@app.route("/")
def index():
    """View function for route /."""
    fmt = "%B %d, %Y, %H:%M:%S %p"
    # time = timezone(str(get_timezone())).strftime(fmt)
    time = datetime.now(timezone(str(get_timezone())))
    return render_template("index.html", time=time.strftime(fmt))


if __name__ == "__main__":
    app.run(debug=True)
