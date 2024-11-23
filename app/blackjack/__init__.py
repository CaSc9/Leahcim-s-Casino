from flask import Blueprint

blackjack_bp = Blueprint('main', __name__, template_folder='templates', static_folder='static')

