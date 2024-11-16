from models.customer import Customer
from models.order import Order
from models.product import Product
from models.orderProduct import order_product
from sqlalchemy import select, func
from sqlalchemy.orm import Session
from database import db
from models.schemas.orderSchema import orders_schema

def save(order_data):
    with Session(db.engine) as session:
        with session.begin():
            # products = [{ "id": product['id'], "qty": product['qty']} for product in order_data['products']]
            # print('Product Id-Qty for order:', products)
            # product_ids = [product['id'] for product in products]
            # print('Product IDs for order:', product_ids)
            product_ids = [product['id'] for product in order_data['products']]
            products = session.execute(select(Product).where(Product.id.in_(product_ids))).scalars().all()

            customer_id = order_data['customer_id']
            customer = session.execute(select(Customer).where(Customer.id == customer_id)).scalars().first()

            if len(products) != len(product_ids):
                raise ValueError("One or more products do not exist")

            if not customer:
                raise ValueError(f'Customer with ID {customer_id} not found.')
            
            new_order = Order(customer_id=order_data['customer_id'], products=products, quantity=order_data['quantity'], date=order_data['date'], total_price=order_data['total_price'])
            
            session.add(new_order)
            print('New Order ID (before commit):', new_order.id)
            session.flush()
            print('New Order ID (after commit):', new_order.id)
            session.commit()

        session.refresh(new_order)

        for product in new_order.products:
            session.refresh(product)

        return new_order
    
def get():
    with Session(db.engine) as session:
        with session.begin():
            orders = session.query(Order).all()
            json_orders = orders_schema.jsonify(orders).json
            return json_orders

# secondary method to get all orders     
# def find_all():
#     query = select(Order)
#     orders = db.session.execute(query).scalars().all() 
#     return orders

def find_all_pagination(page=1, per_page=10):
    orders = db.paginate(select(Order), page=page, per_page=per_page)
    return orders

def top_sellers(): 
# Calculates total quantity of products ordered for each product_id. Ordered by descending order (top is first)
    with Session(db.engine) as session:
        with session.begin():

            # query = session.query(Order).join(order_product).join(Product).filter((order_product.c.order_id == Order.id) & (order_product.c.product_id == Product.id)).all()
            # --- Attempt at joining Order, order_product, Product tables and filtering data --- #

            query = select(Product.id.label('product_id'), func.sum(Order.quantity).label('total_quantity')).select_from(Order).where(Product.id == Order.products).group_by(Product.id)
            # --- This query returns the correct response for 1 product (the first response it can). 


            # Query printout:

            # SELECT products.id AS product_id, sum(orders.quantity) AS total_quantity 
            # FROM orders, products, order_product AS order_product_1       # Note: it only queries 'order_product_1'. Unsure how to allow it to query all items or a different item in the order_product list
            # WHERE products.id = (orders.id = order_product_1.order_id AND products.id = order_product_1.product_id) 
            # GROUP BY products.id

            

            print(query)
            result = db.session.execute(query).all()

            print(result)
            return result