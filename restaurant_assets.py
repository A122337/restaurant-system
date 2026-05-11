# Restaurant Assets and Menu

menu = [
    {"id": 1, "name": "Burger", "price": 25},
    {"id": 2, "name": "Pizza", "price": 35},
    {"id": 3, "name": "Pasta", "price": 30},
    {"id": 4, "name": "Orange Juice", "price": 10}
]

tables = {
    1: "Available",
    2: "Occupied",
    3: "Available",
    4: "Reserved"
}

def show_menu():
    return menu

def check_table(table_number):
    return tables.get(table_number, "Table not found")

def reserve_table(table_number):
    if table_number in tables:
        tables[table_number] = "Reserved"
        return f"Table {table_number} reserved"

    return "Table not found"
