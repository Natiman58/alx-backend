#!/usr/bin/env python3
"""
    To force a particular locale using a user's request
"""

from flask import Flask, render_template, request, g
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


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


@babel.localeselector
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
    return request.accept_languages.best_match(app.config['LANGUAGES'])


# for newer versions of Babel(2.11.0) use this instade of @bable.localeselector
# babel.init_app(app, locale_selector=get_locale)  # add locale_selector

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


@app.route('/', strict_slashes=False)
def index():
    """
    Homepage route
    """
    return render_template('5-index.html')


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
