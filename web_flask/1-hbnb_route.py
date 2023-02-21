#!/usr/bin/python3
''' 1-hbnb_route.py module '''

from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def root_hello():
    '''this function return a simple nessage in root path'''
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb_hello():
    '''this function return a simple nessage in /hbnb path'''
    return 'HBNB'

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
