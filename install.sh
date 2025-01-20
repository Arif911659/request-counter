#!/bin/bash

# Update package database
#!/bin/bash

# Update package database
echo "Updating package database..."
sudo apt update

# Upgrade existing packages
echo "Upgrading existing packages..."
sudo apt upgrade -y

# Build the Docker Image
echo "Building Image.....--->>>"
docker build -t request-counter-app .

# Run the Docker Container
echo "Now run a container based on this image ....>>>>"
echo "Now run a container based on this image ....>>>>"
echo "Now run a container based on this image ....>>>>"
echo "Now run a container based on this image ....>>>>"
docker run -p 5050:5000 request-counter-app

