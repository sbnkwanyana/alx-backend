#!/usr/bin/env python3
"""
Simple flask web app with extension that works with translations
"""


from flask_babel import Babel
from flask import Flask, render_template
from config import Config

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
