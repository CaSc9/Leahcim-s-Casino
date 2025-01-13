from . import db


class Game(db.Model):
    __tablename__ = 'games'

    id = db.Column(db.Integer(), primary_key=True)
    game_code = db.Column(db.String(24), unique=True, nullable=False)
    game_pin = db.Column(db.String(4), nullable=False)
    game_type = db.Column(db.String(), nullable=False)
    game_settings = db.Column(db.String())
    users = db.relationship('User', backref="games", lazy="dynamic")


class User(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer(), primary_key=True)
    username = db.Column(db.String(), unique=True)
    email = db.Column(db.String(), unique=True, nullable=False)
    password = db.Column(db.String(), nullable=False)
    balance = db.Column(db.Integer(), default=1000, nullable=False)
    game_id = db.Column(db.Integer(), db.ForeignKey('games.id'))


