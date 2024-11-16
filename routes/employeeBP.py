from flask import Blueprint
from controllers.employeeController import get, save

employee_blueprint = Blueprint('employee_bp', __name__)
employee_blueprint.route('/', methods=['POST'])(save)
employee_blueprint.route('/', methods=['GET'])(get)