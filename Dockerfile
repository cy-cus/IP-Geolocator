FROM python:3.9

# Set up working directory
WORKDIR /app

# Copy the script to the container
COPY locateip.py /app/locateip.py

# Install dependencies
RUN pip install requests

# Make the script executable
RUN chmod +x /app/locateip.py

# Run the script
ENTRYPOINT ["/usr/local/bin/python", "/app/locateip.py"]
