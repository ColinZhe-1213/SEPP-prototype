from OTPgeneration import OTPgeneration
from OTPvalidation import OTPvalidation

def test_otp_validation_terminal():
    otp_gen = OTPgeneration()
    otp_gen.add_user("user1")
    otp_gen.add_user("user2")
    
    otp1_user1 = otp_gen.generateOTP("user1")
    otp1_user2 = otp_gen.generateOTP("user2")
    print(f"\nGenerated OTP for user1: {otp1_user1}")
    print(f"Generated OTP for user2: {otp1_user2}")
    
    otp_val = OTPvalidation(otp_gen)

    print("\n--- Start testing OTP validation ---")
    input_otp_user1 = input("\nEnter OTP for user1: ")
    otp_val.OTP_validation(input_otp_user1)

    input_otp_user2 = input("\nEnter OTP for user2: ")
    otp_val.OTP_validation(input_otp_user2)

    invalid_otp = input("\nEnter an invalid OTP to test: ")
    otp_val.OTP_validation(invalid_otp)

    otp2_user1 = otp_gen.generateOTP("user1")
    print(f"\nGenerated next OTP for user1: {otp2_user1}")
    input_otp_user1_new = input("\nEnter next OTP for user1 (after counter increment): ")
    otp_val.OTP_validation(input_otp_user1_new)

if __name__ == "__main__":
    test_otp_validation_terminal()
