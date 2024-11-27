# SEPP-prototype
Beginning of Project
---------------------------------------
Idea: 
Language: Python or Java
---------------------------------------
Work unit distribution:

1. Backend Development:<br>
Backend Development Part 1:<br>
Implement OTP Generation<br>
Requirement:<br>
Design the OTP generation function using HMAC with a secret key and counter.<br>
Implement a mock version of SSH Cloud with a REST API to simulate OTP generation.<br>
Ensure that the OTP can be generated based on the user request (with a user ID).<br>
Implement storage of generated OTP in the cloud database (mocked).<br>

Backend Development Part 2:<br>
Implement OTP Validation:<br>
Requirement:<br>
Create an API endpoint to handle OTP validation requests.<br>
Validate the OTP by checking against the stored value in the cloud.<br>
Increment the counter for the next OTP generation.<br>
Record the OTP validation (timestamp, status) in the cloud database.<br>
PIC:<name>

2. Frontend Develoment: <br>
Mockup a simulation environment(2 parts)<br>
Part 1: SSH Hub Simulation:<br>
Requirement:<br>
Mock OTP Request Function<br>
Simulate Backend Response<br>
Simulate Cache<br>
Note:
Simulations are done by <strong>CLI</strong>
Hard-code mock requests with a user ID to interact with the API.

Part 2: Delivery Personnel Simulation:<br>
Requirement:<br>
Simulate OTP Entry<br>
Simulate OTP Validation<br>
Simulate Smart Door Unlock<br>
Note:
*Simulation of OTP entry, otp validation and smart door feature are done by <strong>CLI</strong>
*Simulation for either <strong>success</strong> or <strong>failure case</strong>
PIC:<name>

3. API Developer<br>
Requirement:<br>
Set up a mock REST API<br>
Integrate backend OTP functions<br>
Test endpoints<br>
PIC:<name>

4. Testing and documentation:<br>
Unit Testing<br>
* Each person in charge will need to test if each part of their code is running.(Individually testing)<br>
End-to-End Testing<br>
* Ensure all the codes are compile and working.(As a team testing)<br>
Documentation<br>
* updates on the work units, in- cluding any changes in approach, results of evaluations, etc. as appropriate.(Done individually)<br>




