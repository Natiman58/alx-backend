#!/usr/bin/env python3
"""
This is a simple script to add flak-babel to
the flask application
"""

from flask import Flask, render_template
from flask_babel import Babel


class Config(object):
    """
    Flask configuration for available languages in our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"  # default language
    BABEL_DEFAULT_TIMEZONE = "UTC"  # default timezone


app = Flask(__name__)  # instantiate Flask object
babel = Babel(app)  # instantiate Babel object


@app.route('/', strict_slashes=False)
def homepage():
    """
    Homepage route
    """
    return render_template('1-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
