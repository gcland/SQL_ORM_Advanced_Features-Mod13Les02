from flask import request, jsonify
from models.schemas.orderSchema import order_schema, orders_schema
from services import orderService
from marshmallow import ValidationError

def save(): # post request - contains JSON
    try:
        order_data = order_schema.load(request.json)
        print(order_data)
    except ValidationError as err:
        return jsonify(err.messages), 400
    try:
        order_save = orderService.save(order_data)
        return order_schema.jsonify(order_save), 201
    except ValidationError as e:
        return jsonify({"error":str(e)}), 400
    
def get():
    orders = orderService.get()
    return orders

# secondary method to get all orders
# def find_all():
#     orders = orderService.find_all()
#     return orders_schema.jsonify(orders), 200

def find_all_pagination():
    page = request.args.get('page', 1, type=int)
    per_page = request.args.get('per_page', 10, type=int)
    return orders_schema.jsonify(orderService.find_all_pagination(page=page, per_page=per_page)), 200

def top_sellers(): 
    products = orderService.top_sellers()
    return orders_schema.jsonify(products), 200