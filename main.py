# FLASK_APP=main:app flask run

from flask import Flask

app = Flask(__name__)


def simple_html(text):
    return f"<h1>Wincfarm</h1><p>Animal sound: {text}</p>"


@app.route('/')
def index():
    return simple_html('Hello, world!')


@app.route('/cow')
def cow():
    return simple_html('Meow!')


@app.route('/cat')
def cat():
    return simple_html('Woof!')


if __name__ == "__main__":
    #    app.run(host='0.0.0.0')
    app.run()
