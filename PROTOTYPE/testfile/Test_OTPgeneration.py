import pytest
import os
import json
import tempfile
from code.OTPgeneration import OTPgeneration
USER_DATA_PATH = os.path.join("code", "data", "userdata.json")

#Initialise the test
@pytest.fixture
def test_OTPgeneration():
    otp = OTPgeneration()
    otp.users = {}
    return otp

#test case for OTP sercret generation
def test_generate_OTPsecret():
    otp = OTPgeneration()
    secret = otp.generate_OTPsecret()
    assert len(secret) == 32
    assert secret.isalnum()
    print("Generated OTP secret: " + secret +". \n")
    
#test case for encrypt OTP secret
def test_encrypt_OTPsecret():
    otp = OTPgeneration()
    secret = otp.generate_OTPsecret()
    encrypted_secret = otp.encrypt_OTPsecret(secret)
    assert secret != encrypted_secret
    print("Encrypted OTP secret: " + encrypted_secret.decode() +". \n")

#test case for decrypt OTP secret
def test_decrypt_OTPsecret():
    otp = OTPgeneration()
    secret = otp.generate_OTPsecret()
    encrypted_secret = otp.encrypt_OTPsecret(secret)
    decrypted_secret = otp.decrypt_OTPsecret(encrypted_secret)
    assert secret == decrypted_secret
    print("Decrypted OTP secret: " + decrypted_secret +". \n")

#test case for adding new user and check if the user exists
def test_add_user(test_OTPgeneration):
    otp = OTPgeneration()
    username = "User 1"
    if username in otp.users:
        print("This user " + username+ "exists.\n")
    else:
        otp.add_user(username)
        assert username in otp.users
        print("User " + username + " added successfully.\n")

#test case for deleting user
def test_delete_user():
    otp = OTPgeneration()
    username = "user 1"
    otp.add_user(username)
    if username in otp.users:
        otp.delete_user(username)
        assert username not in otp.users
        print("User " + username + " deleted successfully. \n")
    else:
        print("This user "+ username + " invalid. Unable to delete this user.\n")

#test case for generating OTP first time
def test_generateOTP():
    otp = OTPgeneration()
    username = "user 1"
    otp.add_user(username)
    otp.generateOTP(username)
    otp = otp.generateOTP(username)
    assert otp is not None
    assert len(otp) == 6
    print("OTP generated for user" + username + " is" + otp + ".\n")
    counter = otp.users[username]["counter"]
    assert counter == 1
    print("Counter for user "+ username + " is" + counter + ".\n")

#test case for generating OTP n more times
def test_generateOTPntimes():
    otp = OTPgeneration()
    username = "user 1"
    otp.add_user(username)
    otp1 = otp.generateOTP(username)
    print("OTP generated for user" + username + " is" + otp1 + ".\n")
    otp2 = otp.generateOTP(username)
    assert otp2 is not None
    assert len(otp2) == 6
    print("2nd OTP generated for user" + username + "is " + otp2 + ".\n")    
    counter = otp.users[username]["counter"]
    assert counter == 2
    print("Counter for user "+ username + " is" + counter + ".\n")
    assert otp2 != otp1
    print("First OTP is " + otp1 + "Second OTP is " + otp2 + ".\n")

# Test case for saving user data
def test_save_user_data(test_OTPgeneration):
    otp = test_OTPgeneration
    username = "user 1"
    otp.add_user(username)
    with tempfile.NamedTemporaryFile(delete=False) as testsaveoutput:
        otp.data_file = testsaveoutput.name
        otp.save_user_data()
    with open(testsaveoutput.name, "r") as f:
        data = json.load(f)
        assert username in data
        assert data[username]["counter"] == 0
        print("User data for " + data + " saved successfully.\n")
    os.remove(testsaveoutput.name)

# Test case for loading user data
def test_load_user_data(test_OTPgeneration):
    otp = test_OTPgeneration
    username = "user 1"
    with tempfile.NamedTemporaryFile(delete=False) as testloadoutput:
        user_data = {username: {"counter": 1, "secret": "dummy_secret"}}
        testloadoutput.write(json.dumps(user_data).encode())
        testloadoutput.close()
        otp.data_file = testloadoutput.name
    otp.load_user_data()
    assert username in otp.users
    assert otp.users[username]["counter"] == 1
    assert otp.users[username]["secret"] == "dummy_secret"
    print("User data for " + username + " saved successfully.\n")
    os.remove(testloadoutput.name)

# Test case for displaying user logs
def test_display_log(test_OTPgeneration, capsys):
    otp = test_OTPgeneration
    username = "user 1"
    otp.add_user(username)
    otp.display_log()
    captured = capsys.readouterr()
    assert f"User: {username}" in captured.out
    assert "Counter: 0" in captured.out
<<<<<<< HEAD
    print("Displayed user log successfully.\n")
=======
    print("Displayed user log successfully.\n")
>>>>>>> f10eeb150539e19f7e73d5a5e8a83bb96cfe4399
