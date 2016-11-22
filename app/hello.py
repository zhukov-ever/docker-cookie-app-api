#!flask/bin/python
from flask import Flask

app = Flask(__name__)


@app.route('/test')
def hello():
    return '================ test output 2 ================'


if __name__ == '__main__':
    app.run(host='0.0.0.0')
