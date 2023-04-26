#!/usr/bin/env python3
"""
Simple flask web app with extension that works with translations
"""


from typing import Dict, Union
from flask_babel import Babel
from flask import Flask, render_template, request, g


class Config():
    """
    Babel configuration class
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)

app.config.from_object(Config)

babel = Babel(app)

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@app.route("/")
def index():
    """
    Returns a simple html page
    """
    return render_template("5-index.html")


@babel.localeselector
def get_locale() -> str:
    """
    gets the local of a web request
    """
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


def get_user() -> Union[Dict, None]:
    """
    gets a user
    """
    login_id = request.args.get('login_as')
    if login_id:
        return users.get(int(login_id))
    return None


@app.before_request
def before_request() -> None:
    """
    Performs some routines before each request's resolution.
    """
    user = get_user()
    g.user = user


if __name__ == "__main__":
    """
    Starts the flask app
    """
    app.run()
