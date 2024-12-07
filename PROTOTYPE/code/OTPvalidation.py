import pyotp

class OTPgeneration:

    def OTP_validation(self,username,input_otp):
    # validate the OTP
    #username
        if username not in self.users:
            print(f"User {username} not found")
            return False
    
        user = self.users[username]
        encrypted_secret = user["secret"]
        counter = user["counter"]-1
        secret = self.decrypt_OTPsecret(encrypted_secret)

        hotp = pyotp.HOTP(secret)
        if hotp.verify(input_otp, counter):
            print(f"{username} succeessfully validate the OTP .")
            return True
        else:
            print(f"{username} is failed to validate the OTP.")
            return False
    
    """if we want to check the OTP has expired or not"""
