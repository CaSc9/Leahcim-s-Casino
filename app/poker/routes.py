from flask import render_template, request, redirect, url_for, session, flash
from . import poker_bp
from ..models import Game, User


@poker_bp.route('/game/<game_code>')
def game(game_code):
    game_ref = Game.query.filter_by(game_code=game_code).first()
    if game:
        if 'user' in session and User.query.filter_by(username=session['user']).first() in game_ref.users:
            return render_template('game.html', users=game_ref.users, game=game_ref)

        else:
            flash(f'You are not authorized to play this game.')
            return redirect(url_for('main.join'))

    else:
        flash('This game does not exist')
        return redirect(url_for('main.join'))
