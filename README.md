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
Responsibilities:
OTP Generation: Create a secure function to generate a 6-digit OTP.
Randomization: Utilize HOTP (HMAC-based One-Time Password) for generating unpredictable OTPs.(Phase 1)
Time-based OTP (Optional for Phase 2):If you have time, implement an expiry mechanism for the OTP (e.g., it expires after 5 minutes). This is a common feature in secure OTP systems.(Explore converting HOTP to TOTP with a time-based expiry mechanism if feasible.)
Deliverables:
A function that securely generates a random 6-digit OTP using HOTP.
Unit tests for OTP generation to ensure randomness and security.
PIC: 

Part 2: Implement OTP Validation<br>
Responsibilities:
OTP Validation: Implement the function that takes an OTP input from the user and validates it against the generated OTP.
Match Check: Compare the user input with the stored/generated OTP.
Expiry Validation (Optional): If you implemented expiry in OTP generation, Member 2 would also handle expiry validation (checking if the OTP has expired).(If implemented in Phase 2, handle OTP expiry)
Error Handling: Handle incorrect or expired OTP scenarios. Provide feedback to the user when the OTP is invalid or expired(phase2).
Deliverables:
A function to validate OTPs with proper error handling.
Unit tests for OTP validation, including edge cases like incorrect input or expired OTPs (if implemented).
PIC:

<strong>CLI Interface & User Flow:</strong><br>
Responsibilities:
CLI Interface: Build a simple command-line interface that allows users to either generate an OTP or validate it.
Input Handling: Capture user input for generating or validating OTP.
Output Feedback: Provide feedback after OTP generation and validation (success or failure).(using smart door concept)
Control Flow: Ensure the CLI gives the correct sequence of prompts and responses to the user.
Deliverables:
A CLI application that allows users to generate and validate OTPs.
Clear prompts and outputs simulating the smart door environment.
PIC:

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





Part 2:



CLI Interface & User Flow:
