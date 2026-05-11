# Order Management Module

orders = []

def create_order(order_id, customer_name, items, total_price):
    order = {
        "order_id": order_id,
        "customer_name": customer_name,
        "items": items,
        "total_price": total_price,
        "status": "Preparing"
    }

    orders.append(order)
    return order

def update_order_status(order_id, new_status):
    for order in orders:
        if order["order_id"] == order_id:
            order["status"] = new_status
            return order

    return "Order not found"

def cancel_order(order_id):
    global orders
    orders = [order for order in orders if order["order_id"] != order_id]
    return "Order cancelled"

def get_orders():
    return orders
