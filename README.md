# SEPP-prototype
Beginning of Project
---------------------------------------
Idea: 
Language: Python or Java
---------------------------------------
Work unit distribution:

1. Backend Development:
Part 1: Implement OTP Generation
Design OTP generation using HMAC and a secret key.
Implement a mock version of SSH Cloud with a REST API to simulate OTP generation.
Ensure OTP generation responds with the OTP (and user ID as input).
Simulate storing OTPs in a mock cloud database.

Part 2: Implement OTP Validation
Create an API endpoint to handle OTP validation requests.
Validate OTP by checking it against the stored value in the cloud.
Record the OTP validation process (timestamp, status) and update the counter for the next OTP.
PIC: [Your name]

2. Frontend Development:
Part 1: SSH App Simulation
Hard-code OTP Request Function:
Simulate a user requesting an OTP with a mock user ID.
Simulate the OTP generation through a function call (instead of making an actual API request).
Simulate Displaying OTP:
After generating the OTP, display it as if it came from the backend (mock API).
Simulate Sharing OTP with Delivery Personnel:
The app should display the OTP, simulating the process of sending it to delivery personnel.

Part 2: Delivery Personnel Simulation
Simulate OTP Entry:
Simulate the delivery personnel entering the OTP into a CLI interface.
Simulate OTP Validation:
Upon entering the OTP, simulate an API call to validate the OTP using the mock backend (via an internal function, not a real API).
Simulate Smart Door Unlock:
Based on the validation result, display a message indicating whether the door is unlocked (success) or not (failure).
PIC: [Your name]

3. API Developer:
Set up a mock REST API
Set up two POST endpoints:
POST /generate_otp: Accepts user ID, returns generated OTP.
POST /validate_otp: Accepts OTP and user ID, returns validation status.
Integrate backend OTP functions into these endpoints.
Test the endpoints using Postman or another API testing tool. Verify that the OTPs are correctly generated and validated.
PIC: [API Developer’s name]

4. Testing and documentation:<br>
Unit Testing<br>
* Each person in charge will need to test if each part of their code is running.(Individually testing)<br>
End-to-End Testing<br>
* Ensure all the codes are compile and working.(As a team testing)<br>
Documentation<br>
* updates on the work units, including any changes in approach, results of evaluations, etc. as appropriate.(Done individually)<br>




