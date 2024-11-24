from flask import Blueprint

poker_bp = Blueprint('poker', __name__, template_folder='templates', static_folder='static')
