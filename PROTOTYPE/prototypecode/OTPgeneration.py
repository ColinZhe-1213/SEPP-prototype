import pyotp
from cryptography.fernet import Fernet
import os
import atexit
import json
import datetime
import datetime

class OTPgeneration:
    # Initialize
    def __init__(self):
        self.key = Fernet.generate_key()
        self.fernet = Fernet(self.key)
        self.users = {}
        self.used_otps = set()
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
            self.save_user_data()

    # Delete user
    def delete_user(self, username):
        if username in self.users:
            del self.users[username]
            print("User " + username + " deleted successfully.")
            self.save_user_data()
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
            generation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            otp_entry = {
                "otp": otp,
                "generated_at": generation_time,
                "validated_at": "Not yet validated",
                "status": "active"
            }
            self.users[username]["OTP_history"].append(otp_entry)
            if len(self.users[username]["OTP_history"]) > 1:
                self.users[username]["OTP_history"][0]["status"] = "active"
                for otp_entry in self.users[username]["OTP_history"][:-1]:
                    if otp_entry["validated_at"] == "Not yet validated":
                        otp_entry["status"] = "expired"
            self.users[username]["counter"] += 1
            self.save_user_data()
            return otp
            
    # Mark OTP as used
    def mark_otp_as_used(self, username, otp):
        for otp_entry in self.users[username]["OTP_history"]:
            if otp_entry["otp"] == otp:
                if otp_entry["validated_at"] == "Not yet validated":
                    validation_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                    otp_entry["validated_at"] = validation_time
                    otp_entry["status"] = "validated"
                    self.used_otps.add(otp)
                    self.save_user_data()
                    return True
                else:
                    print("OTP already validated.")
                    return False
        print("OTP is invalid.")
        return False

    # Display user data log
    def display_log(self):
        if not self.users:
            print("No users logs available.")
        else:
            for username, data in self.users.items():
                if data["OTP_history"]:
                    otp_history = ""
                    for otp_entry in data["OTP_history"]:
                        status = otp_entry["status"]
                        if status == "expired":
                            status_message = "Expired"
                        else:
                            status_message = "Validated at: " + otp_entry.get("validated_at", "Not yet validated")
                        otp_history += otp_entry["otp"] + " (Generated at: " + otp_entry["generated_at"] + ", " + status_message + ") \n"
                else:
                    otp_history = "No OTPs generated yet"
                print("User: " + username + " \nCounter: " + str(data['counter']) + " \nSecret (Encrypted): " + data['secret'].decode() + "\nOTP History: " + otp_history + "\n")
       
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
    
    # Display users
    def display_users(self):
        if not self.users:
            print("No users available.")
        else:
            print("List of users:")
            for username in self.users:
                print(username)
                