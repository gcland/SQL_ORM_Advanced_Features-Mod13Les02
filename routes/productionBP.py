from flask import Blueprint
from controllers.productionController import get, save, employee_performance, total_produced

production_blueprint = Blueprint('production_bp', __name__)
production_blueprint.route('/', methods=['POST'])(save)
production_blueprint.route('/', methods=['GET'])(get)
production_blueprint.route('/employee_production', methods=['GET'])(employee_performance)
production_blueprint.route('/total_produced/by-date_produced', methods=['GET'])(total_produced) #/by-date_produced?date_produced=    (example) # Note: DATE MUST BE IN YYYY-DD-MM FORMAT FOR SQL
# Note: DATE MUST BE IN YYYY-DD-MM FORMAT FOR SQL for total_produced/by-date_produced query