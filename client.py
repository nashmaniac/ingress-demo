from flask import Flask

app = Flask(__name__)
title = 'Client'

@app.route('/client/world')
def hello_world():
    return 'Hello World!'

@app.route('/world')
def bro_world():
    return 'Bro World! From %s'%title


@app.route('/nothing/world')
def nothing_world():
    return 'Nothing World! From %s'%title


if __name__ == '__main__':
    app.run(host='0.0.0.0')
