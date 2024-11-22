from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)


@app.route('/')
def index():  # put application's code here
    return render_template('index.html')


@app.route('/login', methods=['GET', 'POST'])
def login():  # put application's code here
    return render_template('login.html')


@app.route('/register', methods=['GET', 'POST'])
def register():  # put application's code here
    return render_template('register.html')


app.route('/game', methods=['GET', 'POST'])
def game():
    return render_template('game.html')


if __name__ == '__main__':
    app.run()
