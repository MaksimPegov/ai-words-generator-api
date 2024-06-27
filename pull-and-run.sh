#!/bin/bash

# Stop the existing Docker container
docker stop words-generator

# Remove the existing Docker container
docker rm words-generator

# Pull the Docker image
docker pull maksimpegov/words-generator

# Run a new Docker container
docker run --name words-generator -d -p 1001:1001 maksimpegov/words-generator