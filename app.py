from flask import Flask
import os

app = Flask(__name__)

@app.route('/')
def hello():
    return "aaaaaaaaaaaaaa"

@app.route('version')
def get_version():
    return "App version : 1.0"

if __name__ == '__main__':
    port = os.environ.get('FLASK_PORT') or 8080
    port = int(port)

    app.run(port=port,host='0.0.0.0')
