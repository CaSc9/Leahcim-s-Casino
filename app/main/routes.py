from flask import render_template, redirect, url_for, request
from . import main_bp


@main_bp.route('/')
def index():
    return render_template('index.html')


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    return render_template('login.html')


@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    return render_template('register.html')


@main_bp.route('/lobby', methods=['GET'])
def lobby():
    game = request.args.get('game')
    if game:
        return redirect(url_for('main.join', game=game))
    return render_template('games-lobby.html')


@main_bp.route('/create', methods=['GET', 'POST'])
def create():
    return render_template('create-game.html')


@main_bp.route('/join', methods=['GET', 'POST'])
def join():
    return render_template('join-game.html', game=request.args.get('game'))
