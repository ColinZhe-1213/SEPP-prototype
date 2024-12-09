# SEPP-prototype
Beginning of Project
---------------------------------------
Idea: OTP generation & validation<br>
Language: Python<br>
---------------------------------------
Work unit distribution:
* We are modifying the prototype into a more consice idea where we just focus on the core concept which is OTP geenration and validation while we used "Smart door unlocking" as our test environment but it will be carried out in terms of CLI instead of GUI.

Before creating main structure, we are creating a <strong>MAKEFILE<strong> first for automating tasks.

<strong>Backend Development:</strong><br>
Part 1: Implement OTP Generation<br>
Responsibilities:<br>
OTP Generation: Create a secure function to generate a 6-digit OTP.<br>
Randomization: Utilize HOTP (HMAC-based One-Time Password) for generating unpredictable OTPs.(Phase 1)<br>
Time-based OTP (Optional for Phase 2):If you have time, implement an expiry mechanism for the OTP (e.g., it expires after 5 minutes). This is a common feature in secure OTP systems.<br>(Explore converting HOTP to TOTP with a time-based expiry mechanism if feasible.)<br>
Deliverables:<br>
A function that securely generates a random 6-digit OTP using HOTP.<br>
Unit tests for OTP generation to ensure randomness and security.<br>
PIC: Colin <br>

Part 2: Implement OTP Validation<br>
Responsibilities:<br>
OTP Validation: Implement the function that takes an OTP input from the user and validates it against the generated OTP.<br>
Match Check: Compare the user input with the stored/generated OTP.<br>
(i) checking the OTP is only digit
Expiry Validation (Optional): If you implemented expiry in OTP generation, Member 2 would also handle expiry validation (checking if the OTP has expired).(If implemented in Phase 2, handle OTP expiry)<br>
Error Handling: Handle incorrect or expired OTP scenarios. Provide feedback to the user when the OTP is invalid or expired(phase2).<br>
Deliverables:<br>
A function to validate OTPs with proper error handling.<br>
Unit tests for OTP validation, including edge cases like incorrect input or expired OTPs (if implemented).<br>
PIC: Keng <br>

<strong>CLI Interface:</strong><br>
Responsibilities:<br>
CLI Interface: Build a simple command-line interface that serves as user interface for interacting with the system that can accomdoate multiple users to manage OTP generation and validation. OTP generation and validation logic will be linked to respective class and not under the CLI class. Door unlocking simulation will be used as a response for successful OTP validation. Also due to multiple user, we will be testing whether all the generated OTPs will be successfully validated instead of each OTP may only be validated by an individual user that generated it.

PIC: Max <br>

<strong>Testing and documentation:</strong><br>
Unit Testing<br>
* Each person in charge will need to test if each part of their code is running.(Individually testing)<br>
End-to-End Testing<br>
* Ensure all the codes are compile and working.(As a team testing)<br>
Documentation<br>
* updates on the work units, including any changes in approach, results of evaluations, etc. as appropriate.(Done individually)<br>

---------------------------------------
Work Updates:<br>
Make File has been fixed with neccessary functions for automations are able to run successfully.<br>
Main.py has been set up and integrate with CLI.py, OTPgeneration,py and OTPvalidation.py.<br>
Users are able to start the program with "make main".<br>

Back end Development:<br>
Part 1:<br>
Complete OTPgeneration (Phase 1). Ensure necesssary functions are working.<br>
Unit test cases has been done and test shown to be pass successfully.<br>
Successfully integrate with CLI and OTPvalidation into Main.py<br>
Phase 1 has been fully completed.(HOTP method).<br>
Transitioning into Phase 2. (TOTP method).<br>


Part 2:<br>
OTP validation (Phase 1) fully completed. Test cases for each functions/ validation cases has been done and pass successfully.<br>
Successfully integrate with CLI and OTPgeneration into Main.py<br>
Transitioning into Phase 2. (TOTP method).<br>

CLI Interface:<br>
CLI Interface has been set up. Integration with neccessary functions are fully integrated.<br>
(Might add designs/colours to make the interface attractive)(Coming up)<br>

Summary
(8/12/2024) We have completed Phase 1 for our OTP system (HOTP).<br>
Coming up: we will be using CI/CD as we move in to Phase 2 (HOTP -> TOTP) to help us automate testing, improve code quality, and ensure seamless integration during the migration.<br>
