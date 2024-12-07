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

            action = menu_options.get(choice)
            if action:
                action()
            else:
                print("Invalid choice. Please try again.")

    def add_user(self):
        username = input("Enter username to add: ").strip()
        if not username:
            print("Username cannot be empty!")
            return
        self.users.add(username)
        print(f"User {username} added successfully.")

    def remove_user(self):
        username = input("Enter username to remove: ").strip()
        if username in self.users:
            self.users.remove(username)
            print(f"User {username} removed successfully.")
        else:
            print(f"User {username} not found.")

    def generate_otp(self):
        username = input("Enter username for OTP generation: ").strip()
        if username in self.users:
            otp = self.otp_handler.generate()  # 需要实际实现
            print(f"OTP for {username}: {otp}")
        else:
            print(f"User {username} not found.")

    def validate_otp(self):
        print("OTP validation functionality is not yet implemented.")

    def list_users(self):
        print("Current users:", ", ".join(self.users))

    def exit_program(self):
        print("Exiting the CLI. Goodbye!")
        exit()


class MockOTPHandler:
    def __init__(self):
        pass

mock_otp_handler = MockOTPHandler()

cli = CLI(mock_otp_handler)

cli.display_menu()