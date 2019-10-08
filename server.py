from flask import Flask

app = Flask(__name__)
title = 'Server'

@app.route('/')
def hello_world():
    return 'Hello World!'

@app.route('/world')
def bro_world():
    return 'Bro World! From %s'%title

if __name__ == '__main__':
    app.run(host='0.0.0.0')
