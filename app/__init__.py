from flask import Flask
from flask_socketio import SocketIO
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate


socketio = SocketIO(cors_allowed_origins='*')
db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config.from_prefixed_env()
    ENV = app.config['ENV']

    app.config.from_object(f'config.{ENV.capitalize()}Config')

    app.config['SQLALCHEMY_DATABASE_URI'] = f"sqlite:///../{app.config['DATABASE_URI']}"

    from app.main import main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    from app.poker import poker_bp
    app.register_blueprint(poker_bp, url_prefix='/poker')

    from app.blackjack import blackjack_bp
    app.register_blueprint(blackjack_bp, url_prefix='/blackjack')

    from app.roulette import roulette_bp
    app.register_blueprint(roulette_bp, url_prefix='/roulette')

    db.init_app(app)
    from app.models import User, Game
    migrate = Migrate(app, db)
    socketio.init_app(app)

    return app
