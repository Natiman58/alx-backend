#!/usr/bin/env python3
"""
    To force a particular locale using a user's request
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel
#from flask.ext.babelex import Babel
from pytz import timezone
import pytz


class Config(object):
    """
    Flask configuration for available languages in our app
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"  # default language
    BABEL_DEFAULT_TIMEZONE = "UTC"  # default timezone


# instantiate objects after configuration
app = Flask(__name__)  # instantiate Flask object
app.config.from_object(Config)
babel = Babel(app)  # instantiate Babel object
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}



#@babel.localeselector
def get_locale():
    """
    Get the current locale
    if the new request lang contains the 'locale' key word
    and if it's in app's language is list
    set the new request language
    if http://127.0.0.1:5000/?locale=fr print 'Bonjour monde!'
    if http://127.0.0.1:5000/?locale=en print 'Hello world!'
    """
    new_lang = request.args.get('locale')
    if new_lang in app.config['LANGUAGES']:
        return new_lang
    if g.user:
        L = g.user.get('locale')
        if L and L in app.config['LANGUAGES']:
            return L
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# for newer versions of Babel(2.11.0) use this instade of @bable.localeselector
babel.init_app(app, locale_selector=get_locale)  # add locale_selector


def get_user():
    """
    Get the current user
    """
    user_id = request.args.get('login_as')
    if user_id:
        return users[int(user_id)]
    return None


@app.before_request
def before_request():
    """
    Before each request check if a user if any exist
    and add it to the global flask.g
    """
    user = get_user()
    g.user = user

# @babel.timezoneselector
def get_timezone() -> str:
    """
        infer appropriate time zone
    """
    # get time zone from url
    tz = request.get('timezone')
    if tz:
        try:
            # check if it's a valid time zone
            return pytz.timezone(tz)
        # catch the exception
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    # get time zone from user
    if g.user:
        try:
            tz = g.user.get('timezone')
            return pytz.timezone(tz)
        except pytz.exceptions.UnknownTimeZoneError:
            pass
    # else Default to UTC
    return app.config.get("BABEL_DEFAULT_TIMEZONE")
babel.init_app(app, timezone_selector=get_timezone)

@app.route('/', strict_slashes=False)
def index():
    """
    Homepage route
    """
    return render_template('7-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
