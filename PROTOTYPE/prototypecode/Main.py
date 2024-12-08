from OTPgeneration import OTPgeneration
from OTPvalidation import OTPvalidation
from Cli import CLI

def main():
    otp_generator = OTPgeneration()
    otp_validator = OTPvalidation(otp_generator)
    cli = CLI(otp_generator, otp_validator)
    cli.display_menu()

if __name__ == "__main__":
    main()