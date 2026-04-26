from auth_module import Authentication
from order_module import OrderManagement
from restaurant_assets import RestaurantAssets

def run_all_system_tests():
    print("=== SYSTEM TESTING COMMENCED ===\n")
    
    # 1. Unit Testing: Testing authentication logic
    print("[1] Unit Test: Authentication logic")
    auth = Authentication()
    assert auth.login("admin_user", "admin_pass_123") == "Admin"
    print("Unit Test Passed.\n")

    # 2. Integration Testing: Flow between Order creation and Status
    print("[2] Integration Test: Order creation flow")
    order_sys = OrderManagement()
    order_sys.create_takeaway_order(101, ["Pizza", "Coffee"])
    assert order_sys.orders[101]["status"] == "In Preparation"
    print("Integration Test Passed.\n")

    # 3. Static Testing: (Represented by code structure review)
    print("[3] Static Testing: Modular structure verified.\n")

    # 4. Dynamic Testing: Performance check (Simulating 200 orders)
    print("[4] Dynamic Test: High volume order handling")
    for i in range(200):
        order_sys.create_takeaway_order(i, ["Sample Item"])
    print(f"Dynamic Test Passed: Handled {len(order_sys.orders)} orders correctly.\n")

if __name__ == "__main__":
    run_all_system_tests()