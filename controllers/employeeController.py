from flask import request, jsonify
from models.employee import Employee
from models.schemas.employeeSchema import employee_schema, employees_schema
from services import employeeService
from marshmallow import ValidationError

def save(): # post request - contains JSON
    try:
        employee_data = employee_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    try:
        employee_save = employeeService.save(employee_data)
        return employee_schema.jsonify(employee_save), 201
    except ValidationError as e:
        return jsonify({"error":str(e)}), 400
    
def get():
    employees = employeeService.get()
    return employees