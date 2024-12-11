import pytest
import os
import json
import tempfile
import datetime
from prototypecode.OTPgeneration import OTPgeneration

USER_DATA_PATH = os.path.join("code", "data", "userdata.json")

@pytest.fixture(scope="function")
# Initialize the test
def test_OTPgeneration():
    otp_gen = OTPgeneration()
    otp_gen.users.clear() 
    return OTPgeneration()

# Test case for generate,encrypt and decrypt OTP secret generation
def test_generate_encrypt_decrypt_OTPsecret():
    otp = OTPgeneration()
    secret = otp.generate_OTPsecret()# Generate OTP secret
    assert len(secret) == 32
    assert secret.isalnum()
    print("Test passed: Generated OTP secret: " + secret + ".\n")
    encrypted_secret = otp.encrypt_OTPsecret(secret)# Encrypt the OTP secret
    assert secret != encrypted_secret
    print("Test passed: Encrypted OTP secret: " + encrypted_secret.decode() + ".\n")
    decrypted_secret = otp.decrypt_OTPsecret(encrypted_secret)# Decrypt the OTP secret
    assert secret == decrypted_secret
    print("Test passed: Decrypted OTP secret: " + decrypted_secret + ".\n")

# Test case for adding new user
def test_add_user(test_OTPgeneration):
    otp = test_OTPgeneration
    username = "user1"
    otp.add_user(username)
    assert username in otp.users, f"Expected {username} to be in users, but it's not."
    assert otp.users[username]["counter"] == 0, f"Expected counter to be 0, but got {otp.users[username]['counter']}."
    assert otp.users[username]["OTP_history"] == []
 
# Test case for adding existing user
def test_add_user_existing_user(test_OTPgeneration, capsys):
    otp = test_OTPgeneration
    username = "user1"
    otp.add_user(username)
    otp.add_user(username)
    captured = capsys.readouterr()
    assert f"User {username} already exists." in captured.out
    assert otp.users[username]["counter"] == 0
    assert otp.users[username]["OTP_history"] == []


# Test case for deleting a user
def test_delete_user(test_OTPgeneration, capsys):
    otp = test_OTPgeneration
    username = "user 1" 
    otp.add_user(username)
    otp.delete_user(username)
    assert username not in otp.users
    print("Test passed: User " + username + " deleted successfully.\n")
    
# Test case for deleting a nonexistent user
def test_delete_nonexistent_user(test_OTPgeneration, capsys):
    otp = test_OTPgeneration
    otp.delete_user("nonexistent_user")
    captured = capsys.readouterr()
    assert "not found" in captured.out
    print("Test passed: Unable to delete non existing user.\n")

# Test case for generating OTP the first time
def test_generate_otp(test_OTPgeneration):
    otp = test_OTPgeneration
    username = "user 1"
    otp.add_user(username)
    generated_otp = otp.generateOTP(username)
    assert generated_otp is not None
    assert len(generated_otp) == 6
    print("Test passed: Generated OTP for " + username + ": " + generated_otp + ".\n")

# Test case for generating OTP for a nonexistent user
def test_generate_otp_for_nonexistent_user(test_OTPgeneration, capsys):
    otp = test_OTPgeneration
    otp.generateOTP("nonexistent_user")
    captured = capsys.readouterr()
    assert "Username not found" in captured.out
    print("Test passed: Generate OTP fail! User not found.\n")

# Test case for generating OTP n times
def test_generateOTP_n_times(test_OTPgeneration):
    otp = test_OTPgeneration
    username = "user1"
    otp.add_user(username)
    otp1 = otp.generateOTP(username)
    otp2 = otp.generateOTP(username)
    assert len(otp1) == 6
    assert len(otp2) == 6
    assert otp1 != otp2
    assert otp.users[username]["counter"] == 2
    assert otp.users[username]["OTP_history"] == [otp1, otp2]
    print("Test passed.\n")

# Test case for saving and loading user data to a file
def test_save_and_load_user_data(test_OTPgeneration, tmp_path):
    otp = test_OTPgeneration
    username = "user 1"
    otp.add_user(username)
    temp_file = tmp_path / "userdata.json"
    otp.data_file_path = str(temp_file)
    otp.save_user_data()
    otp.users.clear()
    otp.load_user_data()
    assert username in otp.users
    print("Test passed: User data saved and loaded successfully for " + username + ".\n")

# Test case for displaying user logs
def test_display_log(test_OTPgeneration, capsys):
    otp = test_OTPgeneration
    username = "user1"
    otp.add_user(username)
    otp.display_log()
    captured = capsys.readouterr()
    assert "User: user1" in captured.out
    print("Test passed: User log displayed correctly.\n")
    
# Test case for display empty user
def test_display_users_empty(test_OTPgeneration, capsys):
    otp = test_OTPgeneration
    otp.users.clear()
    otp.display_users()
    captured = capsys.readouterr()
    assert "No users available" in captured.out
    print("Test passed: There is no users.\n")

# Test case for display user with users
def test_display_users_with_users(test_OTPgeneration, capsys):
    otp = test_OTPgeneration
    added_users = ["user1", "user2"]
    for user in added_users:
        otp.add_user(user)
    otp.display_users()
    captured = capsys.readouterr()
    assert "List of users:" in captured.out
    for user in added_users:
        assert user in captured.out
    print("Test passed: Users are " + ', '.join(added_users) + ".\n")

# Test case for OTP history
def test_otp_history(test_OTPgeneration):
    otp = test_OTPgeneration
    username = "user1"
    otp.add_user(username)
    otp1 = otp.generateOTP(username)
    otp2 = otp.generateOTP(username)
    assert len(otp1) == 6
    assert len(otp2) == 6
    otp_history = otp.users[username]["OTP_history"]
    assert otp_history[-2:] == [otp1, otp2], f"Expected OTP history to be {[otp1, otp2]}, but got {otp_history[-2:]}"
    assert otp_history[-2:] == [otp1, otp2]
    print("Test passed: OTP history for " + username + ": " + str(otp.users[username]["OTP_history"]) + ".")