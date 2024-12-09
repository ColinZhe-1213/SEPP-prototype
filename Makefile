# Python environment
PYTHON := python3.12
PIP := pip3

TEST_DIR = PROTOTYPE/prototypecode
SRC_DIR = PROTOTYPE/prototypecode

# Install dependencies
install:
	@echo "Installing dependencies"
	$(PIP) install --upgrade pip
	$(PIP) install -r requirement.txt
endif

# Run tests using pytest
test:
	@echo "Running tests"
	export PYTHONPATH=$(PWD)/$(TEST_DIR) && $(PYTHON) -m pytest -s $(TEST_DIR)

# Clean up temporary files
clean:
	@echo "Cleaning files"
	find . -name "__pycache__" -type d -exec rm -rf {} +
	find . -name ".pytest_cache" -type d -exec rm -rf {} +

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

# Run Main
main: 
	@echo "Launching Main"
	$(PYTHON) $(SRC_DIR)/Main.py

# Show help
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  install       Install dependencies"
	@echo "  test          Run tests"
	@echo "  clean         Clean temporary files"
	@echo "  generateOTP   Run OTP generation script"
	@echo "  validateOTP   Run OTP validation script"
	@echo "  cli           Launch CLI"
	@echo "  main          Launch Main script"
