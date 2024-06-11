# Use Red Hat Universal Base Image (UBI) as a base image
FROM registry.access.redhat.com/ubi9/python-311

# Set environment variables for Flask
ENV FLASK_APP=python-api-debug.py
ENV FLASK_RUN_HOST=0.0.0.0
ENV FLASK_RUN_PORT=5000

# Set the working directory in the container
WORKDIR /app

# Copy the current directory contents into the container at /app
COPY . .

# Install Flask and its dependencies
RUN pip install --no-cache-dir Flask

# Expose the Flask port
EXPOSE 5000

# Command to run the Flask application
CMD ["flask", "run"]