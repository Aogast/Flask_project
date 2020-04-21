from flask import Flask, url_for, request, render_template, redirect

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('main.html')


if __name__ == '__main__':
    app.run(port=8080, host='127.0.0.1')
