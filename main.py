import os
import requests
from flask import Flask
app = Flask(__name__)

MYAPPINFO = os.getenv('MYAPPINFO')
URL = os.getenv('URL')


@app.route('/home')
def home():
    return MYAPPINFO


@app.route('/curl')
def curl():
    response = requests.get(URL)
    response = response.text
    return response


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port=3000)
