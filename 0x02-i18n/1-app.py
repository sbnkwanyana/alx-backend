#!/usr/bin/env python3
"""
Simple flask web app with extension that works with translations
"""


from flask_babel import Babel
from flask import Flask, render_template


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
    return render_template("1-index.html")


if __name__ == "__main__":
    """
    Starts the flask app
    """
    app.run()
