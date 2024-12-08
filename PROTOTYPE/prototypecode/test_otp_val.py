import pytest
from OTPgeneration import OTPgeneration
from OTPvalidation import OTPvalidation

def test_otp_validation():
def test_otp_validation():
    otp_gen = OTPgeneration()
    otp_gen.add_user("user 1")
    otp_gen.add_user("user 2")
    
    otp1_user1 = otp_gen.generateOTP("user 1")
    otp1_user2 = otp_gen.generateOTP("user 2")
    print("OTP for user 1: " + otp1_user1)
    print("OTP for user 2: " + otp1_user2)
    
    otp_val = OTPvalidation(otp_gen)
    print("Testing OTP validation...")
    
    assert otp_val.OTP_validation(otp1_user1) is True, "Valid OTP for user1 failed"
    print("Test case passed: OTP for user 1 is valid.")
    
    assert otp_val.OTP_validation(otp1_user2) is True, "Valid OTP for user2 failed"
    print("Test case passed: OTP for user 2 is valid.")
    
    invalid_otp = "123456"
    assert otp_val.OTP_validation(invalid_otp) is False, "Invalid OTP should fail"
    print("Test case passed: Invalid OTP fails.")

    otp2_user1 = otp_gen.generateOTP("user 1")

    assert otp_val.OTP_validation(otp1_user1) is False, "Expired OTP for user 1 should fail"
    print("Test case passed: OTP for user1 is expired.")

    assert otp_val.OTP_validation(otp2_user1) is True, "Second OTP for user 1 should be valid"
    print("Test case passed: OTP for user 1 is valid after regeneration.")

    lessthan6digitOTP = "1233"
    assert otp_val.OTP_validation(lessthan6digitOTP) is False, "Less than 6 digits OTP should fail"
    print("Test case passed: OTP is less than 6 digits.")

    morethan6digitOTP = "1234567"
    assert otp_val.OTP_validation(morethan6digitOTP) is False, "More than 6 digits OTP should fail"
    print("Test case passed: OTP is more than 6 digits.")
    
    non_numeric_otp = "ABC123"
    assert otp_val.OTP_validation(non_numeric_otp) is False, "OTP should only contain digits"
    print("Test case passed: OTP with non-numeric characters fails.")