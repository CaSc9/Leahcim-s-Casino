from flask import render_template, url_for
from . import main_bp


@main_bp.route('/')
def index():  # put poker_application's code here
    return render_template('index.html')


@main_bp.route('/login', methods=['GET', 'POST'])
def login():  # put poker_application's code here
    return render_template('templates/login.html')


@main_bp.route('/register', methods=['GET', 'POST'])
def register():  # put main_application's code here
    return render_template('templates/register.html')


@main_bp.route('/game', methods=['GET', 'POST'])
def game():
    return render_template('templates/game.html')
