#!/usr/bin/env python3
"""
    A script to setup a flask application
"""

from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def hello():
    """
    Renders the home page
    """
    return render_template('0-index.html')
