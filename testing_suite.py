# Testing Suite

from auth_module import login
from order_module import create_order, update_order_status
from restaurant_assets import show_menu

def run_tests():

    print("Testing Login...")
    print(login("admin", "1234"))

    print("\nTesting Order Creation...")
    order = create_order(
        1,
        "Ahmed",
        ["Burger", "Pizza"],
        60
    )

    print(order)

    print("\nTesting Order Status Update...")
    updated_order = update_order_status(1, "Ready")
    print(updated_order)

    print("\nTesting Menu Display...")
    print(show_menu())

if __name__ == "__main__":
    run_tests()
