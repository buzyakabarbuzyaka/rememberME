from flask import Flask

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'


def start():
    app.run(host='0.0.0.0', port=5000)


if __name__ == '__main__':
    start()