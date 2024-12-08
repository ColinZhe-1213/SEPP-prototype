import pyotp
from OTPgeneration import OTPgeneration
class OTPvalidation:

    #initialize
    def __init__(self, otp_generation_instance):
        self.otp_gen = otp_generation_instance

    def OTP_validation(self, input_otp):
        # Validate the OTP format
        if not input_otp.isdigit():
            print("!OTP MUST BE DIGIT！")
            return False
        elif len(input_otp) != 6:
            print("!OTP MUST BE 6 DIGITS!")
            return False

        # Loop through all users to check if the OTP is valid for any user
        for username, user in self.otp_gen.users.items():
            encrypted_secret = user["secret"]
            counter_before_increment = user["counter"] - 1
            secret = self.otp_gen.decrypt_OTPsecret(encrypted_secret)
            hotp = pyotp.HOTP(secret)
            generated_otp = hotp.at(counter_before_increment)

            # Check if OTP matches and hasn't been used
            if input_otp == generated_otp:
                if input_otp not in self.otp_gen.used_otps:
                    print(f"OTP is valid for user {username}, smart door unlocked")
                    self.otp_gen.mark_otp_as_used(username, input_otp)
                    return True
                else:
                    print("OTP has already been used.")
                    return False

        print("OTP is invalid, OTP not found or already used, smart door locked")
        return False
