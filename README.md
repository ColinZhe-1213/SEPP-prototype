# SEPP-prototype
Beginning of Project
---------------------------------------
Idea: OTP generation & validation<br>
Language: Python<br>
---------------------------------------
Work unit distribution:
* We are modifying the prototype into a more consice idea where we just focus on the core concept which is OTP geenration and validation while we used "Smart door unlocking" as our test environment but it will be carried out in terms of CLI instead of GUI.

<strong>Backend Development:</strong><br>
Part 1: Implement OTP Generation<br>
Responsibilities:<br>
OTP Generation: Create a secure function to generate a 6-digit OTP.<br>
Randomization: Utilize HOTP (HMAC-based One-Time Password) for generating unpredictable OTPs.(Phase 1)<br>
Time-based OTP (Optional for Phase 2):If you have time, implement an expiry mechanism for the OTP (e.g., it expires after 5 minutes). This is a common feature in secure OTP systems.<br>(Explore converting HOTP to TOTP with a time-based expiry mechanism if feasible.)<br>
Deliverables:<br>
A function that securely generates a random 6-digit OTP using HOTP.<br>
Unit tests for OTP generation to ensure randomness and security.<br>
PIC: <name> <br>

Part 2: Implement OTP Validation<br>
Responsibilities:<br>
OTP Validation: Implement the function that takes an OTP input from the user and validates it against the generated OTP.<br>
Match Check: Compare the user input with the stored/generated OTP.<br>
Expiry Validation (Optional): If you implemented expiry in OTP generation, Member 2 would also handle expiry validation (checking if the OTP has expired).(If implemented in Phase 2, handle OTP expiry)<br>
Error Handling: Handle incorrect or expired OTP scenarios. Provide feedback to the user when the OTP is invalid or expired(phase2).<br>
Deliverables:<br>
A function to validate OTPs with proper error handling.<br>
Unit tests for OTP validation, including edge cases like incorrect input or expired OTPs (if implemented).<br>
PIC:<name><br>

<strong>CLI Interface & User Flow:</strong><br>
Responsibilities:<br>
CLI Interface: Build a simple command-line interface that allows users to either generate an OTP or validate it.<br>
Input Handling: Capture user input for generating or validating OTP.<br>
Output Feedback: Provide feedback after OTP generation and validation (success or failure).(using smart door concept)<br>
Control Flow: Ensure the CLI gives the correct sequence of prompts and responses to the user.<br>
Deliverables:<br>
A CLI application that allows users to generate and validate OTPs.<br>
Clear prompts and outputs simulating the smart door environment.<br>
PIC:<name <br>

<strong>Testing and documentation:</strong><br>
Unit Testing<br>
* Each person in charge will need to test if each part of their code is running.(Individually testing)<br>
End-to-End Testing<br>
* Ensure all the codes are compile and working.(As a team testing)<br>
Documentation<br>
* updates on the work units, including any changes in approach, results of evaluations, etc. as appropriate.(Done individually)<br>

---------------------------------------
Work Updates:

Back end Development:
Part 1:
Start the skeleton fram for OTP geenration(HOTP method)




Part 2:



CLI Interface & User Flow:
