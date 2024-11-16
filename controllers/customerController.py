from flask import request, jsonify
from models.customer import Customer
from models.schemas.customerSchema import customer_schema, customers_schema
from services import customerService
from marshmallow import ValidationError

def save(): # post request - contains JSON
    try:
        customer_data = customer_schema.load(request.json)
    except ValidationError as err:
        return jsonify(err.messages), 400
    try:
        customer_save = customerService.save(customer_data)
        return customer_schema.jsonify(customer_save), 201
    except ValidationError as e:
        return jsonify({"error":str(e)}), 400
    
def get():
    customers = customerService.get()
    return customers

def total_value(): 
    result = customerService.total_value()
    print(result)
    return customers_schema.jsonify(result), 200