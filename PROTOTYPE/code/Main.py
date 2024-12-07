import pyotp

new_secret = pyotp.random_base32()
print(f"Generated Secret: {new_secret}")
