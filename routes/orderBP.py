from flask import Blueprint
from controllers.orderController import get, save, find_all_pagination, top_sellers

order_blueprint = Blueprint('order_bp', __name__)
order_blueprint.route('/', methods=['POST'])(save)
order_blueprint.route('/', methods=['GET'])(get)
order_blueprint.route('/paginate', methods=['GET'])(find_all_pagination)
order_blueprint.route('/top_sellers', methods=['GET'])(top_sellers)