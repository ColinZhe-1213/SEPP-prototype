import pyotp
from PROTOTYPE.prototypecode.OTPgeneration import OTPgeneration
from PROTOTYPE.prototypecode.OTPvalidation import OTPvalidation
from colorama import Fore, Style
from colorama import init
class CLI:
    def __init__(self, otp_generator,otp_validator):
        self.otp_generator = otp_generator
        self.otp_validator = otp_validator

    def display_menu(self):
        print(Fore.CYAN + "\nWelcome to the simulated environment!")
        print(Fore.CYAN + "-------------------------------------")

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
            print(Fore.LIGHTWHITE_EX + "\nPlease select an option:\n")
            print(Fore.GREEN + "1. Add a User")
            print(Fore.GREEN + "2. Remove a User")
            print(Fore.GREEN + "3. Generate OTP for a User")
            print(Fore.GREEN + "4. Validate OTP")
            print(Fore.GREEN + "5. List All Users")
            print(Fore.GREEN + "6. Display Logs")
            print(Fore.GREEN + "7. Exit\n")
            choice = input(Fore.LIGHTRED_EX + "Please enter your choice: " + Fore.WHITE)

            action = menu_options.get(choice)
            if action:
                action()
            else:
                print(Fore.LIGHTMAGENTA_EX + "Invalid choice. Please try again.")

    def add_user(self):
        username = input(Fore.LIGHTYELLOW_EX + "Enter username to add: " + Fore.RESET).strip()
        if username == "":
            print(Fore.MAGENTA + "Username cannot be empty!")
            return
        self.otp_generator.add_user(username)

    def remove_user(self):
        username = input(Fore.LIGHTYELLOW_EX + "Enter username to remove: " + Fore.RESET).strip() 
        self.otp_generator.delete_user(username)

    def generate_otp(self):
        username = input(Fore.LIGHTYELLOW_EX + "Enter username for OTP generation: " + Fore.RESET).strip()
        otp = self.otp_generator.generateOTP(username)
        if otp:
            print(Fore.LIGHTMAGENTA_EX + "OTP for " + username + " is " + otp + "." + Fore.RESET)

    def validate_otp(self):
        otp = input(Fore.LIGHTYELLOW_EX + "Enter the OTP to validate: " + Fore.RESET).strip()
        if otp == "":
            print(Fore.LIGHTMAGENTA_EX + "OTP cannot be empty!" + Fore.RESET)
            return
        is_valid = self.otp_validator.OTP_validation(otp)

    def list_users(self):
        self.otp_generator.display_users()
    
    def display_logs(self):
        self.otp_generator.display_log()

    def exit_program(self):
        print(Fore.LIGHTBLUE_EX + "Goodbye!\n" + Fore.RESET)
        exit()
        
otp_generator = OTPgeneration()
otp_validator = OTPvalidation(otp_generator)
cli = CLI(otp_generator, otp_validator)


