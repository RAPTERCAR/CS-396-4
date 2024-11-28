# Use Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the client script
COPY client.py /app/

# Expose the port(s) the client may use
EXPOSE 15002/tcp

# Command to run the client script
CMD ["python", "client.py"]
