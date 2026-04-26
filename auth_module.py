import hashlib

class Authentication:
    """
    Handles user login, password encryption, and role-based access control.
    """
    def __init__(self):
        # Initial user data with encrypted passwords (SHA-256)
        self.users = {
            "admin_user": {
                "password": self._encrypt_password("admin_pass_123"), 
                "role": "Admin"
            },
            "staff_member": {
                "password": self._encrypt_password("staff_pass_456"), 
                "role": "Waiter"
            }
        }

    def _encrypt_password(self, password):
        """Encrypts the password using SHA-256 for security."""
        return hashlib.sha256(password.encode()).hexdigest()

    def login(self, username, password):
        """Authenticates the user and returns their role if valid."""
        encrypted_input = self._encrypt_password(password)
        
        if username in self.users and self.users[username]["password"] == encrypted_input:
            print(f"User {username} authenticated successfully as {self.users[username]['role']}.")
            return self.users[username]["role"]
        
        print("Authentication failed: Invalid credentials.")
        return None