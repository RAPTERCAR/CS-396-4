# Use Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the multiply script
COPY multiply.py /app/

# Expose the ports the multiply service uses
EXPOSE 15002/tcp

# Command to run the multiply script
CMD ["python", "multiply.py"]
