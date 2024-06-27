#!/bin/bash

# docker login -u maksimpegov

docker build --platform linux/amd64 --build-arg OPENAI_API_KEY=$(grep OPENAI_API_KEY .env | cut -d '=' -f2) -t words-generator:latest .

docker tag words-generator:latest maksimpegov/words-generator

docker push maksimpegov/words-generator