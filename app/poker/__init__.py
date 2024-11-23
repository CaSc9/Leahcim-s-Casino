from flask import Blueprint

poker_bp = Blueprint('main', __name__, template_folder='templates', static_folder='static')


