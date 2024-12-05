# Python environment settings
PYTHON = python3.12
PIP = pip3
TEST_DIR = testfile
SRC_DIR = code

# Install dependencies
install:
	@echo "Dependencies installing"
	$(PIP) install -r requirement.txt

# Run tests using unittest
test:
	@echo "Running test"
	$(PYTHON) -m unittest discover $(TEST_DIR)

# Clean up temporary files
clean:
	@echo "Cleaning files"
	rm -rf __pycache__ .pytest_cache

# Lint for identifying code error
lint:
	$(PYTHON) -m flake8 $(SRC_DIR)

#Run OTP generation script
generateOTP:
	@echo "Generating OTP"
	$(PYTHON) $(SRC_DIR)/OTPgeneration.py

# Run OTP validation script
validateOTP:
	@echo "Validating OTP"
	$(PYTHON) $(SRC_DIR)/OTPvalidation.py

# Run CLI 
cli:
	@echo "Launching CLI"
	$(PYTHON) $(SRC_DIR)/Cli.py
