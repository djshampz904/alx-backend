#!/usr/bin/env python3
""" Basic Flask app, Basic Babel setup, Get locale from request,
from flask import Flask, render_template, request
"""
from flask import Flask, render_template, request

app = Flask(__name__)


@app.route('/')
def index():
    """ Returns index """
    return render_template('0-index.html')


if __name__ == "__main__":
    app.run()
