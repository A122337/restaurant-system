class RestaurantAssets:
    """
    Manages table statuses and menu items.
    """
    def __init__(self):
        # Table statuses: Available, Reserved, Occupied
        self.tables = {1: "Available", 2: "Available", 3: "Available"}
        self.menu = {"Pizza": 15.0, "Coffee": 3.5, "Burger": 10.0}

    def update_table_status(self, table_number, status):
        """Updates table status (e.g., after customer leaves)."""
        if table_number in self.tables:
            self.tables[table_number] = status
            print(f"Table {table_number} is now {status}.")

    def add_menu_item(self, item_name, price):
        """Allows Admin to add new items to the menu."""
        self.menu[item_name] = price
        print(f"Added {item_name} to the menu at ${price}.")