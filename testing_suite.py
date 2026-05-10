from order_module import create_order, update_order_status
from restaurant_assets import add_menu_item

def test_create_order():
    order = create_order("takeaway", ["Burger"])
    assert order is not None

def test_update_status():
    create_order("takeaway", ["Pizza"])
    assert update_order_status(102, "preparing") == True

def test_add_menu():
    add_menu_item("Pasta", 30)

test_create_order()
test_update_status()
test_add_menu()

print("All tests passed")