from flask import Flask
from flask_socketio import SocketIO


socketio = SocketIO(cors_allowed_origins='*')


def create_app():

    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'SECRET'
    app.debug = True

    from app.main import main_bp
    app.register_blueprint(main_bp, url_prefix='/')

    socketio.init_app(app)
    return app

