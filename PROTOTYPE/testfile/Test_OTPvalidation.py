import unittest

from code.OTPvalidation import OTPgeneration


class TestOTPValidation(unittest.TestCase):
    def setUp(self):
        # initialize the environment
        self.otp = OTPgeneration()
        self.otp.users = {
            "keng": {"secret": "6RTJJH254RNQNM63", "counter": 10},
            "colin": {"secret": "JXIOUYPCHV6QMNM5", "counter": 5}
              }
        #decrypt_OTPsecret
        self.otp.decrypt_OTPsecret = lambda secret: secret

    #test the OTP is true
    def test_OTP_true(self):
        true_otp = "654321"
        result = self.otp.OTP_validation("keng",true_otp)
        self.assertTrue(result, "OTP is valid")
    #test the OTP is false
    def test_OTP_false(self):
        result = self.otp.OTP_validation("keng", "243561") 
        self.assertFalse(result, "OTP is invalid")
    #test the OTP is NOT digit
    def test_OTP_NONDigit(self):
        result = self.otp.OTP_validation("keng", "xyz246")
        self.assertFalse(result, "OTP is invalid,cannot contain nondigit")
    #test the length != 6    
    def test_OTP_lengthis_NOT6(self):
        result = self.otp.OTP_validation("keng", "54321") 
        self.assertFalse(result, "OTP must be 6 digits ")
    #test the user is not exits
    def test_user_missing(self):
        result = self.otp.OTP_validation("Ali", "654321")  
        self.assertFalse(result, "OTP the user is missing")
    #test the counter
    def test_OTP_counter(self):
        true_otp = "654321" #assume that
        result = self.otp.OTP_validation("keng", true_otp)
        self.assertTrue(result, "OTP is valid")
    #test OTP for multiple users 
    def test_validate_otp_with_multiple_users(self):
        result = self.otp.OTP_validation("colin", "666555")  
        self.assertFalse(result, "OTP is invalid")
        
        result = self.otp.OTP_validation("keng", "654321")
        self.assertTrue(result, "OTP is valid")
    
if __name__ == '__main__':
    unittest.main()