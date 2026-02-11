# Start from the ubuntu image
FROM ubuntu:24.04

#install curl
RUN apt-get update && apt-get install -y curl

# Use /usr/src/app as our workdir
WORKDIR /usr/src/app

# Copy the script.sh file and make it executable
COPY script.sh .
RUN chmod +x script.sh

# Create additional file
RUN touch additional.txt

# Run the script
ENTRYPOINT  ["./script.sh"]