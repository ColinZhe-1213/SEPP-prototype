# Python environment settings
PYTHON = python3
PIP = pip3
TEST_DIR = testfile
SRC_DIR = code

# Install dependencies
install:
	$(PIP) install -r requirement.txt

# Run tests using unittest
test:
	$(PYTHON) -m unittest discover $(TEST_DIR)

# Clean up temporary files
clean:
	rm -rf __pycache__ .pytest_cache

# Run Linting (optional, requires flake8 or other linting tools)
lint:
	$(PYTHON) -m flake8 $(SRC_DIR)