FROM ubuntu:20.04
RUN apt-get update && apt-get install -y libstdc++6

# Use the official Python image as the base image
FROM python:3.11-slim


RUN apt-get update && apt-get install -y \
    gcc \
    libc6\
    python3-dev \
    libhdf5-dev \
    pkg-config \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Set up working directory
WORKDIR /app

# Install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt


# Copy the rest of your application code
COPY . .
# Make port 80 available to the world outside this container
EXPOSE 80

# Define environment variable
ENV FLASK_APP=app.py

# Run app.py when the container launches
CMD ["flask", "run", "--host=0.0.0.0", "--port=80"]