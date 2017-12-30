#coding=utf8

from flask import Flask
from flask import jsonify
from flask_cors import CORS
from flask import request
import time

app = Flask(__name__)
CORS(app)


def cls(message):
    prob = 0.05
    is_spam = 0
    time.sleep(5)
    return {'prob': prob, 'is_spam': is_spam}


@app.route('/api/message', methods = ['POST', 'GET'])
def message():
    if request.method == 'GET':
        return 'hello'
    if request.method == 'POST':
        req = request.json
        message = req.get('message')
        return jsonify(cls(message))

if __name__ == '__main__':
    app.run(debug=True)