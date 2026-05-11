# Authentication Module

users = {
    "admin": "1234",
    "manager": "5678"
}

def login(username, password):
    if username in users and users[username] == password:
        return True
    return False

def logout():
    return "User logged out successfully"

def register(username, password):
    if username in users:
        return "User already exists"
    
    users[username] = password
    return "User registered successfully"
