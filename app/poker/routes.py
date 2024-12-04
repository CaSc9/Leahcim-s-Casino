from flask import render_template
from . import poker_bp


@poker_bp.route('/game')
def game():
    return render_template('game.html')
