# Docker configuration
DOCKER_IMAGE = prototype
DOCKER_RUN = docker run --rm -v $(PWD):/app -w /app $(DOCKER_IMAGE)

# Python environment
PYTHON := python3.12
PIP := pip3

# Directories
SRC_DIR = PROTOTYPE/prototypecode
TEST_DIR = PROTOTYPE/prototypecode

# Build Docker image
docker-build:
	@echo "Building Docker image"
	docker build -t $(DOCKER_IMAGE) .

# Install dependencies inside Docker container
install:
	@echo "Installing dependencies"
	$(DOCKER_RUN) $(PIP) install -r requirements.txt

# Run tests using pytest
test:
	@echo "Running tests"
	$(DOCKER_RUN) sh -c "export PYTHONPATH=/app/PROTOTYPE/prototypecode && $(PYTHON) -m pytest -s $(TEST_DIR)"

# Clean up temporary files
clean:
	@echo "Cleaning files"
	$(DOCKER_RUN) sh -c "find . -name '__pycache__' -type d -exec rm -rf {} +"
	$(DOCKER_RUN) sh -c "find . -name '.pytest_cache' -type d -exec rm -rf {} +"

# Run OTP generation script
generateOTP:
	@echo "Generating OTP"
	$(DOCKER_RUN) $(PYTHON) $(SRC_DIR)/OTPgeneration.py

# Run OTP validation script
validateOTP:
	@echo "Validating OTP"
	$(DOCKER_RUN) $(PYTHON) $(SRC_DIR)/OTPvalidation.py

# Run CLI
cli:
	@echo "Launching CLI"
	$(DOCKER_RUN) $(PYTHON) $(SRC_DIR)/Cli.py

# Run Main script
main:
	@echo "Launching Main"
	docker run -it --rm -v $(PWD):/app -w /app prototype python3 /app/PROTOTYPE/prototypecode/Main.py


# Show help
.PHONY: help
help:
	@echo "Available targets:"
	@echo "  docker-build  Build the Docker image"
	@echo "  install       Install dependencies"
	@echo "  test          Run tests"
	@echo "  clean         Clean temporary files"
	@echo "  generateOTP   Run OTP generation script"
	@echo "  validateOTP   Run OTP validation script"
	@echo "  cli           Launch CLI"
	@echo "  main          Launch Main script"
