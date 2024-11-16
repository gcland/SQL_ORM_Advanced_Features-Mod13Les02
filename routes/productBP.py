from flask import Blueprint
from controllers.productController import get, save, find_all_pagination

product_blueprint = Blueprint('product_bp', __name__)
product_blueprint.route('/', methods=['POST'])(save)
product_blueprint.route('/', methods=['GET'])(get)
product_blueprint.route('/paginate', methods=['GET'])(find_all_pagination)