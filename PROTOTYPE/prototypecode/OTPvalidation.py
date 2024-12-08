import pyotp
from OTPgeneration import OTPgeneration
class OTPvalidation:

    #initialize
    def __init__(self, otp_generation_instance):
        self.otp_gen = otp_generation_instance

    def OTP_validation(self,input_otp):
    # validate the OTP format
    
        #OTP SHOULD BE 6 DIGIT 
        if not input_otp.isdigit():
            print("!OTP MUST BE DIGIT！")
            return False
        elif len(input_otp) !=6:
            print("!OTP MUST BE 6 DIGITS!")
            return False
        
        for username,user in self.otp_gen.users.items():
            encrypted_secret = user["secret"]
            counter = user["counter"]
            secret = self.decrypt_OTPsecret(encrypted_secret)
            hotp = pyotp.HOTP(secret)

            if hotp.verify(input_otp, counter):
                self.otp_gen.users[username]["counter"] += 1
                print(f"{username} succeessfully validate the OTP .")
                return True
            else:
                print(f"{username} is failed to validate the OTP.")
                return False
    """if we want to check the OTP has expired or not"""
