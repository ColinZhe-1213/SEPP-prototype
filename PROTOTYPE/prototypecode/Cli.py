import pyotp
from OTPgeneration import OTPgeneration
from OTPvalidation import OTPvalidation

class CLI:
    def __init__(self, otp_generator,otp_validator):
        self.otp_generator = otp_generator
        self.otp_validator = otp_validator

    def display_menu(self):
        print("Welcome to the simulated environment!")
        print("-------------------------------------")

        menu_options = {
            "1": self.add_user,
            "2": self.remove_user,
            "3": self.generate_otp,
            "4": self.validate_otp,
            "5": self.list_users,
            "6": self.display_logs,
            "7": self.exit_program
        }

        while True:
            print("\nMain Menu:")
            print("1. Add a User")
            print("2. Remove a User")
            print("3. Generate OTP for a User")
            print("4. Validate OTP")
            print("5. List All Users")
            print("6. Display Logs")
            print("7. Exit")
            choice = input("Please enter your choice: ")

            action = menu_options.get(choice)
            if action:
                action()
            else:
                print("Invalid choice. Please try again.")

    def add_user(self):
        username = input("Enter username to add: ").strip()
        if username == "":
            print("Username cannot be empty!")
            return
        self.otp_generator.add_user(username)


    def remove_user(self):
        username = input("Enter username to remove: ").strip() 
        self.otp_generator.delete_user(username)

    def generate_otp(self):
        username = input("Enter username for OTP generation: ").strip()
        otp = self.otp_generator.generateOTP(username)
        if otp:
            print("OTP for " + username + " is " + otp + ".")

    def validate_otp(self):
        otp = input("Enter the OTP to validate: ").strip()
        if otp == "":
            print("OTP cannot be empty!")
            return
        is_valid = self.otp_validator.OTP_validation(otp)
        if is_valid:
            print(f"The OTP '{otp}' is valid.")
        else:
            print(f"The OTP '{otp}' is invalid or expired.")

    def list_users(self):
        self.otp_generator.display_users()
    
    def display_logs(self):
        self.otp_generator.display_log()

    def exit_program(self):
        print("Exiting the environment. Goodbye!")
        exit()
        
otp_generator = OTPgeneration()
otp_validator = OTPvalidation()
cli = CLI(otp_generator, otp_validator)


