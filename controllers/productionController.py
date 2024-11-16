from flask import request, jsonify
from models.production import Production
from models.schemas.productionSchema import production_schema, productions_schema
from services import productionService
from marshmallow import ValidationError

def save(): # post request - contains JSON
    try:
        production_data = production_schema.load(request.json)
        print(production_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    try:
        production_save = productionService.save(production_data)
        return production_schema.jsonify(production_save), 201
    except ValidationError as e:
        return jsonify({"error":str(e)}), 400
    
def get():
    productions = productionService.get()
    return productions

def employee_performance(): 
    employees = productionService.employee_performance()
    print(employees)
    return productions_schema.jsonify(employees), 200

def total_produced(): 
    date = request.args.get('date_produced')
    result = productionService.total_produced(date)
    print(result)
    return productions_schema.jsonify(result), 200