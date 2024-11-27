# SEPP-prototype
Beginning of Project
---------------------------------------
Idea: OTP generation & validation<br>
Language: Python<br>
---------------------------------------
Work unit distribution:

<strong>Backend Development:</strong><br>
Part 1: Implement OTP Generation<br>
Design OTP generation using HMAC and a secret key.<br>
Implement a mock version of SSH Cloud with a REST API to simulate OTP generation.<br>
Ensure OTP generation responds with the OTP (and user ID as input).<br>
Simulate storing OTPs in a mock cloud database.<br>

Part 2: Implement OTP Validation<br>
Create an API endpoint to handle OTP validation requests.<br>
Validate OTP by checking it against the stored value in the cloud.<br>
Record the OTP validation process (timestamp, status) and update the counter for the next OTP.<br>
PIC: Colin<br>

<strong>Frontend Development:</strong><br>

Part 1: SSH App Simulation<br>
Hard-code OTP Request Function:<br>
Simulate a user requesting an OTP with a mock user ID.<br>
Simulate the OTP generation through a function call (instead of making an actual API request).<br>
Simulate Displaying OTP:<br>
After generating the OTP, display it as if it came from the backend (mock API).<br>
Simulate Sharing OTP with Delivery Personnel:<br>
The app should display the OTP, simulating the process of sending it to delivery personnel.<br>

Part 2: Delivery Personnel Simulation<br>
Simulate OTP Entry:<br>
Simulate the delivery personnel entering the OTP into a CLI interface.<br>
Simulate OTP Validation:<br>
Upon entering the OTP, simulate an API call to validate the OTP using the mock backend (via an internal function, not a real API).<br>
Simulate Smart Door Unlock:<br>
Based on the validation result, display a message indicating whether the door is unlocked (success) or not (failure).<br>
PIC: Keng Xiang <br>

<strong>API Developer:</strong><br>
Set up a mock REST API<br>
Set up two POST endpoints:<br>
POST /generate_otp: Accepts user ID, returns generated OTP.<br>
POST /validate_otp: Accepts OTP and user ID, returns validation status.<br>
Integrate backend OTP functions into these endpoints.<br>
Test the endpoints using Postman or another API testing tool. Verify that the OTPs are correctly generated and validated.<br>
PIC: Max <br>

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



Front-end Development:

Part 1:




Part 2:



API Development: