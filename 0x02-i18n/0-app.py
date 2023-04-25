#!/usr/bin/env python3
"""
Simple flask web app. Run by using flask --app 0-app.py run
"""


from flask import Flask, render_template


app = Flask(__name__)


@app.route("/")
def index():
    """
    Returns a simple html page
    """
    return render_template("0-index.html")


if __name__ == "__main__":
    """
    Starts the flask app
    """
    app.run()
