currentUser = None

def initApp():
    print("System initialized")

def login():
    global currentUser
    currentUser = {"id": "001", "role": "manager"}
    print("Logged in")

def logout():
    global currentUser
    currentUser = None
    print("Logged out")