import pyotp
from cryptography.fernet import Fernet
import os
import atexit
import json

class OTPgeneration:
    # Initialize
    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        self.users = {}
        self.data_file_path = os.path.join(os.getcwd(), "data", "userdata.json")
        self.load_user_data()
        atexit.register(self.reset_json_data)

    # Generate random OTP secret
    def generate_OTPsecret(self):
        return pyotp.random_base32()
    
    # Encrypt OTP Secret
    def encrypt_OTPsecret(self,OTP):
        encrypted = self.fernet.encrypt(OTP.encode())
        return encrypted
    
    # Decrypt OTP Secret
    def decrypt_OTPsecret(self,OTP):
        decrypted = self.fernet.decrypt(OTP)
        return decrypted.decode()
     
    # Add user
    def add_user(self,username):
        if username in self.users:
            print("User " + username + " already exists.")
        else:
            secret = self.generate_OTPsecret()
            encrypted_secret = self.fernet.encrypt(secret.encode())
            self.users[username] = {
                "secret": encrypted_secret,
                "counter": 0,
                "OTP_history": []
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
    def generateOTP(self,username):
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
            self.users[username]["OTP_history"].append(otp)
            self.users[username]["counter"] += 1
            return otp
    
    # Display user data log
    def display_log(self):
        for username, data in self.users.items():
            otp_history = ', '.join(data["OTP_history"]) if data["OTP_history"] else "No OTPs generated yet"
            print(f"User: {username}, Counter: {data['counter']}, Secret (Encrypted): {data['secret']}, OTP History: {otp_history}")
    
    # Reset user data
    def reset_json_data(self):
        self.save_user_data()
        self.clear_json_file()
        self.users.clear()
        print("Clearing all memory.")
        
    # Save user data
    def save_user_data(self):
        os.makedirs(os.path.dirname(self.data_file_path), exist_ok=True)
        with open(self.data_file_path, "w") as f:
            users_to_save = {
                username: {
                    "secret": self.decrypt_OTPsecret(user["secret"]),
                    "counter": user["counter"],
                    "OTP_history": user["OTP_history"]
                } for username, user in self.users.items()
            }
            json.dump(users_to_save, f, indent=4)
        print("User data saved.")
    
    # Load user data
    def load_user_data(self):
        if os.path.exists(self.data_file_path):
            with open(self.data_file_path, "r") as f:
                loaded_data = json.load(f)
            for username, data in loaded_data.items():
                otp_history = data.get("OTP_history", [])
                counter = data.get("counter", 1)
                secret = data["secret"]
                encrypted_secret = self.fernet.encrypt(data["secret"].encode())
                self.users[username] = {
                    "secret": encrypted_secret,
                    "counter": counter,
                    "OTP_history": otp_history
                }
            print("User data loaded.")
        else:
            print("New program is starting.")
    
    #clear all the data
    def clear_json_file(self):
        with open(self.data_file_path, "w") as f:
            json.dump({}, f, indent=4)
        print("Clear User data.")