#!/usr/bin/python3
''' hello world file '''

from flask import Flask


app = Flask(__name__)
app.url_map.strict_slashes = False

@app.route('/')
def hello_world():
    ''' listen in / '''
    return 'Hello HBNB!' 

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)