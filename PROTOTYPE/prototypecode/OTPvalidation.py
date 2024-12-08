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
            counter_before_increment = user["counter"] - 1
            secret = self.otp_gen.decrypt_OTPsecret(encrypted_secret)
            hotp = pyotp.HOTP(secret)
            generated_otp = hotp.at(counter_before_increment)

            if input_otp == generated_otp:
                print("OTP is valid, smart door unlock")
                return True
            
        print("OTP is invalid ,OTP not found or already used, smart door locked")
        return False



    """if we want to check the OTP has expired or not"""
