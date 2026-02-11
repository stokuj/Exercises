#!/bin/bash

# Exit immediately if a command exits with a non-zero status.
# This ensures the script stops if the clone or build fails.
set -e

# Capture arguments into variables for readability
GITHUB_REPO=$1
DOCKER_REPO=$2

# Check if arguments were supplied
if [ -z "$GITHUB_REPO" ] || [ -z "$DOCKER_REPO" ]; then
    echo "Error: Missing arguments."
    echo "Usage: ./builder.sh <github_repo> <docker_hub_repo>"
    exit 1
fi

# Define a temporary directory name to avoid naming conflicts
TEMP_DIR="temp_build_dir"

# Clean up any existing temp dir from previous failed runs
if [ -d "$TEMP_DIR" ]; then
    rm -rf "$TEMP_DIR"
fi

echo "--- Process Started ---"

# 1. Clone the repository
# We construct the full URL using the first argument
echo "1. Cloning https://github.com/$GITHUB_REPO..."
git clone "https://github.com/$GITHUB_REPO.git" $TEMP_DIR

# Move into the directory
cd $TEMP_DIR

# 2. Build the Docker image
# We tag it (-t) with the Docker Hub repo name (second argument) immediately
echo "2. Building image $DOCKER_REPO..."
docker build -t $DOCKER_REPO .

# 3. Push to Docker Hub
# Note: You must be logged in via 'docker login' before running this script
echo "3. Pushing image to Docker Hub..."
docker push $DOCKER_REPO

# Cleanup: Move back out and remove the temporary directory
cd ..
rm -rf $TEMP_DIR

echo "--- Success! Image published to $DOCKER_REPO ---"