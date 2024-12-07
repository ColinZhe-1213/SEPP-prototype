import pyotp
from cryptography.fernet import Fernet
import os
import atexit

class OTPgeneration:
    # Initialize
    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        self.users = {}
        atexit.register(self.clear_user_data)
        
    # Generate random OTP secret
    def generate_OTPsecret(self):
        return pyotp.random_base32()
    
    # Encrypt OTP Secret
    def encrypt_OTPsecret(self, OTP):
        encrypted = self.fernet.encrypt(OTP.encode())
        return encrypted
    
    # Decrypt OTP Secret
    def decrypt_OTPsecret(self, OTP):
        decrypted = self.fernet.decrypt(OTP)
        return decrypted.decode()
     
    # Add user
    def add_user(self, username):
        if username in self.users:
            print("User " + username + " already exists.")
        else:
            secret = self.generate_OTPsecret()
            encrypted_secret = self.fernet.encrypt(secret.encode())
            self.users[username] = {
                "secret": encrypted_secret,
                "counter": 1 
            }
            print("User " + username + " added successfully.")
    
    # Delete user
    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
            print("User " + username + " deleted successfully.")
        else:
            print("User " + username + " not found.")
    
    # Generate OTP for each user
    def generateOTP(self, username):
        if username not in self.users:
            print("Username not found")
            return None
        else:
            user = self.users[username]
            encrypted_secret = user["secret"]
            counter = user["counter"]
            secret = self.decrypt_OTPsecret(encrypted_secret)
            hotp = pyotp.HOTP(secret)
            otp = hotp.at(counter)
            self.users[username]["counter"] += 1
            return otp
    
    # Display user data log
    def display_log(self):
        for username, data in self.users.items():
            print("User: " + username + ", Counter: " + str(data["counter"]) + ", Secret (Encrypted): " + str(data["secret"]))

    # Clear user data (called when the program exits)
    def clear_user_data(self):
        print("Clearing user data...")
        self.users.clear()  # Clear all users in memory
        print("User data cleared.")
