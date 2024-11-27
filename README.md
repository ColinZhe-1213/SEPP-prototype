# SEPP-prototype
Beginning of Project
---------------------------------------
Idea: ???
Language: Python or Java
---------------------------------------
Work unit distribution:

1. Backend Development:
Backend Development Part 1:
Implement OTP Generation
Requirement:
Design the OTP generation function using HMAC with a secret key and counter.
Implement a mock version of SSH Cloud with a REST API to simulate OTP generation.
Ensure that the OTP can be generated based on the user request (with a user ID).
Implement storage of generated OTP in the cloud database (mocked).

Backend Development Part 2:
Implement OTP Validation:
Requirement:
Create an API endpoint to handle OTP validation requests.
Validate the OTP by checking against the stored value in the cloud.
Increment the counter for the next OTP generation.
Record the OTP validation (timestamp, status) in the cloud database.

2. Frontend Develoment: 
Mockup a simulation environment(2 parts)
Part 1: SSH Hub Simulation:
Requirement:
Mock OTP Request Function
Simulate Backend Response
Simulate Cache

Part 2: Delivery Personnel Simulation:
Requirement:
Simulate OTP Entry
Simulate OTP Validation
Simulate Smart Door Unlock(via command approve or decline)

3. Testing and documentation:
Unit Testing
End-to-End Testing
Documentation



