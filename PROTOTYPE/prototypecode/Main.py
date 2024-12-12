from PROTOTYPE.prototypecode.OTPgeneration import OTPgeneration
from PROTOTYPE.prototypecode.OTPvalidation import OTPvalidation
from PROTOTYPE.prototypecode.Cli import CLI

def main():
    otp_generator = OTPgeneration()
    otp_validator = OTPvalidation(otp_generator)
    cli = CLI(otp_generator, otp_validator)
    cli.display_menu()

if __name__ == "__main__":
    main()