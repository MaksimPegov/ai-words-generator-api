#!/bin/bash

# Stop the existing Docker container
docker stop words-generator

# Remove the existing Docker container
docker rm words-generator

# Rebuild the Docker image
docker build --build-arg OPENAI_API_KEY=$(grep OPENAI_API_KEY .env | cut -d '=' -f2) -t words-generator:latest .

# Run a new Docker container
docker run --name words-generator -d -p 1001:1001 words-generator:latest