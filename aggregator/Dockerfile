# Use Python base image
FROM python:3.9-slim

# Set the working directory
WORKDIR /app

# Copy the aggregator script
COPY aggregator.py /app/

# Expose the port for the aggregator
EXPOSE 15012/tcp

# Command to run the aggregator script
CMD ["python", "aggregator.py"]
