#!/usr/bin/env python3
"""
Simple flask web app with extension that works with translations
"""


from flask_babel import Babel
from flask import Flask, render_template, request


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


@app.route("/")
def index():
    """
    Returns a simple html page
    """
    return render_template("4-index.html")


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


if __name__ == "__main__":
    """
    Starts the flask app
    """
    app.run()
