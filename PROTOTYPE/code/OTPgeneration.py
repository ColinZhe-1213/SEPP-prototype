import pyotp
from cryptography.fernet import Fernet
import json
import atexit 
import os

class OTPgeneration:
    # Initialize
    def __init__(self,data_directory="code/data", json_filename="userdata.json"):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        self.data_directory = data_directory
        self.json_filename = json_filename
        os.makedirs(self.data_directory, exist_ok=True)
        self.users = self.load_users_from_file()
        atexit.register(self.reset_json_data)
        
    #Generate random OTP secret
    def generate_OTPsecret(self):
        return pyotp.random_base32()
    
    #Encrypt OTP Secret
    def encrypt_OTPsecret(self,OTP):
        encrypted = self.fernet.encrypt(OTP.encode())
        return encrypted
    
    #Decrypt OTP Secret
    def decrypt_OTPsecret(self,OTP):
        decrypted = self.fernet.decrypt(OTP)
        return decrypted.decode()
     
    #Add user
    def add_user(self,username):
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
    
    #Delete user
    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
            print("User " + username + " deleted successfully.")
        else:
            print("User " + username + " not found.")
    
    #Generate OTP for each user
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
            self.users[username]["counter"] += 1
            return otp
    
    #Save the user data into JSON
    def save_user_data(self):
        with open(self.data_file, "w") as f:
            json.dump(self.users, f, indent=4)
    
    #Load the user data from JSON
    def load_user_data(self):
        if os.path.exists(self.data_file):
            with open(self.get_file_path(), "r") as file:
                return json.load(file)
        else:
            print("FileNotFoundError")
            return {}
    
    #Display user data log
    def display_log(self):
        for username, data in self.users.items():
             print("User: " + username + ", Counter: " + str(data["counter"]) + ", Secret (Encrypted): " + data["secret"])



 