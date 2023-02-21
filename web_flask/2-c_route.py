#!/usr/bin/python3
''' 2-c_route module '''

from flask import Flask
from markupsafe import escape

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root_hello():
    '''this function return a simple nessage in root path'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_hello():
    '''this function return a simple nessage in /hbnb path'''
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_is_fun(text):
    '''this function return a string whith underscore symbol remplaced as space'''
    new_text = text.remplace('_', ' ')
    return f"C + {escape(new_text)}"


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
