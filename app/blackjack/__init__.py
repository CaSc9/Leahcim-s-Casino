from flask import Blueprint

blackjack_bp = Blueprint('blackjack', __name__, template_folder='templates', static_folder='static')
