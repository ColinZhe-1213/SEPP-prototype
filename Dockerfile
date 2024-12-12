# Base image
FROM python:3.12-slim

# Install tools
RUN apt-get update && apt-get install -y \
    make \
    gcc \
    g++ \
    python3-dev \
    && apt-get clean

# Set the working directory inside the container
WORKDIR /app

# Copy requirement.txt and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the application files
COPY . /app

# Set default command to run Main.py
CMD ["python", "PROTOTYPE/prototypecode/Main.py"]
