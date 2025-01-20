# Use an official Python runtime as the base image
FROM python:3.9-slim

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file into the container
COPY requirements.txt .

# Install the required packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy the Python script into the container
COPY app.py .

# Set an environment variable (you can override this when running the container)
ENV FLASK_ENV=production

# Expose the port the app runs on
EXPOSE 5000

# Run the Python script when the container launches
CMD ["python", "app.py"]

