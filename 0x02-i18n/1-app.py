#!/usr/bin/env python3
"""
This is a simple script to add flak-babel to
the flask application
"""

from flask import Flask
from flask_babel import Babel

app = Flask(__name__)  # instantiate Flask object
app.config.from_object(app.Config)
babel = Babel(app)  # instantiate Bable object


class Config(object):
    """
    Flask configuration for available languages in our app
    """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'  # default language
    BABEL_DEFAULT_TIMEZONE = 'UTC'  # default timezone
