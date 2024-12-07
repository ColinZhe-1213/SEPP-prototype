import pyotp

class CLI:
    def __init__(self, otp_handler):
        self.otp_handler = otp_handler
        self.users = set() 

    def display_menu(self):
        print("Welcome to Smart Door Unlocking CLI!")
        print("-------------------------------------")

        menu_options = {
            "1": self.add_user,
            "2": self.remove_user,
            "3": self.generate_otp,
            "4": self.validate_otp,
            "5": self.list_users,
            "6": self.exit_program
        }

        while True:
            print("\nMain Menu:")
            print("1. Add a User")
            print("2. Remove a User")
            print("3. Generate OTP for a User")
            print("4. Validate OTP for a User")
            print("5. List All Users")
            print("6. Exit")
            choice = input("Please enter your choice: ")

            if choice == "1":
                self.add_user()
            elif choice == "2":
                self.remove_user()
            elif choice == "3":
                self.generate_otp()
            elif choice == "4":
                self.validate_otp()
            elif choice == "5":
                self.list_users()
            elif choice == "6":
                print("Exiting the CLI. Goodbye!")
                break
            else:
                print("Invalid choice. Please try again.")

class MockOTPHandler:
    def __init__(self):
        pass

mock_otp_handler = MockOTPHandler()

cli = CLI(mock_otp_handler)

cli.display_menu()