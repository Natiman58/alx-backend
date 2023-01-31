#!/usr/bin/env python3
"""
This is a simple script to make flask recognize the default
language configuration
"""

from flask import Flask, render_template, request
from flask_babel import Babel


class Config:
    """
    Flask configuration for available languages in our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"  # default language
    BABEL_DEFAULT_TIMEZONE = "UTC"  # default timezone


app = Flask(__name__)  # instantiate Flask object
app.config.from_object(Config)
babel = Babel(app)  # instantiate Babel object


@babel.localeselector
def get_locale():
    """
    Get the current locale
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


#babel.init_app(app, locale_selector=get_locale)  # add locale_selector


@app.route('/', strict_slashes=False)
def index():
    """
    Homepage route
    """
    return render_template('3-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
