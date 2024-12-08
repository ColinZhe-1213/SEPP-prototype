# Python environment settings
PYTHON = python3.12
PIP = pip3
TEST_DIR = PROTOTYPE/prototypecode
SRC_DIR = PROTOTYPE/prototypecode

# Install dependencies
install:
	@echo "Installing dependencies"
	$(PIP) install -r requirements.txt

# Run tests using pytest
test:
	@echo "Running tests"
	export PYTHONPATH=$(PWD)/PROTOTYPE/prototypecode && $(PYTHON) -m pytest $(TEST_DIR)

# Clean up temporary files
clean:
	@echo "Cleaning files"
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name ".pytest_cache" -type d -exec rm -rf {} +

# Lint for identifying code errors
lint:
	$(PYTHON) -m flake8 $(SRC_DIR)

# Run OTP generation script
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
