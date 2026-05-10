orders = []
orderCounter = 100

def create_order(order_type, items, table_id=None):
    global orderCounter
    orderCounter += 1

    order = {
        "orderNum": orderCounter,
        "type": order_type,
        "tableId": table_id,
        "items": items,
        "status": "new"
    }

    orders.append(order)
    return order

def update_order_status(order_num, new_status):
    for order in orders:
        if order["orderNum"] == order_num:
            order["status"] = new_status
            return True
    return False

def display_orders():
    for order in orders:
        print(order)

def show_kitchen_orders():
    for order in orders:
        if order["status"] in ["new", "preparing"]:
            print(order)

def show_table_order(table_id):
    for order in orders:
        if order["tableId"] == table_id:
            print(order)