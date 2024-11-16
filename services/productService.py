from sqlalchemy.orm import Session
from sqlalchemy import select, func
from database import db
from models.product import Product
from models.schemas.productSchema import products_schema

def save(product_data):
    with Session(db.engine) as session:
        with session.begin():
            new_product = Product(name=product_data['name'], price=product_data['price'])
            session.add(new_product)
            session.commit()

        session.refresh(new_product)
        return new_product
    
def get():
    with Session(db.engine) as session:
        with session.begin():
            products = session.query(Product).all()
            json_products = products_schema.jsonify(products).json
            return json_products
        
def find_all_pagination(page=1, per_page=10):
    products = db.paginate(select(Product), page=page, per_page=per_page)
    return products

