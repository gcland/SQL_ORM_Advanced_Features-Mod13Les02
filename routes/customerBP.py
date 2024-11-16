from flask import Blueprint
from controllers.customerController import get, save, total_value

customer_blueprint = Blueprint('customer_bp', __name__)
customer_blueprint.route('/', methods=['POST'])(save)
customer_blueprint.route('/', methods=['GET'])(get)
customer_blueprint.route('/total_value', methods=['GET'])(total_value)