from flask import render_template
from . import main_bp


@main_bp.route('/')
def index():  # put poker_application's code here
    return render_template('index.html')


@main_bp.route('/login', methods=['GET', 'POST'])
def login():  # put poker_application's code here
    return render_template('login.html')


@main_bp.route('/register', methods=['GET', 'POST'])
def register():  # put main_application's code here
    return render_template('register.html')
