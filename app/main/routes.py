from flask import render_template, redirect, url_for, request, session, flash
from . import main_bp
from ..models import Game, User
from .. import db
import uuid


@main_bp.route('/')
def index():
    if 'user' in session: return redirect(url_for('main.lobby'))
    return render_template('index.html')


@main_bp.route('/login', methods=['GET', 'POST'])
def login():
    if 'user' in session: return redirect(url_for('main.lobby'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        user = User.query.filter_by(username=username).first()
        if user and password == user.password:
            session['user'] = username
            return redirect(url_for('main.lobby'))
        else:
            flash('Invalid username or password')
            return redirect(url_for('main.login'))
    else:
        return render_template('login.html')


@main_bp.route('/register', methods=['GET', 'POST'])
def register():
    if 'user' in session: return redirect(url_for('main.lobby'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        email = request.form['email']
        if User.query.filter_by(username=username).first():
            flash('User already exists')
            return redirect(url_for('main.login'))
        else:
            new_user = User(username=username, password=password, email=email)
            db.session.add(new_user)
            db.session.commit()

            session['user'] = username

        return redirect(url_for('main.lobby'))
    else:
        return render_template('register.html')


@main_bp.route('/lobby', methods=['GET'])
def lobby():
    if 'user' in session:
        game = request.args.get('game')
        if game:
            return redirect(url_for('main.join', game=game))
        return render_template('games-lobby.html')
    return redirect(url_for('main.login'))


@main_bp.route('/create', methods=['GET', 'POST'])
def create():
    if 'user' in session:
        if request.method == 'POST':
            game_code = session['code']
            session.pop('code')
            pin = request.form['pin']
            game_typ = request.form['game-typ']
            settings = ';'.join([request.form['limit'], request.form['big-blind']])
            if Game.query.filter_by(game_code=game_code).first():
                flash('Game already exists')
                return redirect(url_for('main.join', code=game_code))
            else:
                new_game = Game(game_code=game_code, game_type=game_typ, game_pin=pin, game_settings=settings)
                db.session.add(new_game)
                new_game.users.append(User.query.filter_by(username=session['user']).first())
                db.session.commit()

                session['game'] = game_code
                return redirect(url_for('poker.game', game_code=game_code))

        else:
            game = request.args.get('game')
            code = uuid.uuid4().hex[:24]
            session['code'] = code
            return render_template('create-game.html', game=game, game_code=code)
    else:
        return redirect(url_for('main.login'))


@main_bp.route('/join', methods=['GET', 'POST'])
def join():
    if 'user' in session:
        if request.method == 'POST':
            game_code = request.form['game-code']
            game_pin = request.form['pin']
            game_type = request.form['game-typ']
            game = Game.query.filter_by(game_code=game_code).first()
            if game.users.count() > 7:
                flash('Game is full...')
                return render_template('join.html')
            if game and game.game_pin == game_pin:
                game.users.append(User.query.filter_by(username=session['user']).first())
                db.session.commit()
                if game_type == 'poker':
                    session['game'] = game_code
                    return redirect(url_for('poker.game', game_code=game_code))
                # More Game Pages redirects
            else:
                flash('Invalid game code or pin')
                return render_template('join-game.html', game=game_type)
        else:
            game = request.args.get('game')
            game_pin = request.args.get('pin')
            game_code = request.args.get('code')
            return render_template('join-game.html', game=game, code=game_code, pin=game_pin)
    else:
        return redirect(url_for('main.login'))
