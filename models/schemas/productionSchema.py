from marshmallow import fields
from schema import ma

class ProductionSchema(ma.Schema):
    id = fields.Integer(required=False)
    date_produced = fields.Date(required=True)
    product_id = fields.Integer(required=True)
    employee_id = fields.Integer(required=True)
    quantity_produced = fields.Integer(required=True)

    class Meta:
        fields = ("id", "date_produced", "employee_id", "product_id", "quantity_produced", "total_quantity", "total_produced")

production_schema = ProductionSchema()
productions_schema = ProductionSchema(many=True)