#!/bin/bash
# Get the URL from the command line arguments
url=$1

# Use curl to send a request to the URL and get the size of the response body
response_size=$(curl -sI "$url" | grep -i Content-Length | awk '{print $2}')

# Display the size in bytes
echo "$response_size"
