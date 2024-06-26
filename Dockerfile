# Using lightweight alpine image
FROM python:3.10-alpine

# Installing packages
RUN apk update
RUN pip install --no-cache-dir pipenv

# Defining working directory and adding source code
WORKDIR /usr/src/words-gen-api
COPY Pipfile Pipfile.lock start.sh ./
COPY main ./main

# Install API dependencies
RUN pipenv install --system --deploy

ARG OPENAI_API_KEY
ENV OPENAI_API_KEY=$OPENAI_API_KEY

# Start app
EXPOSE 1001
ENTRYPOINT ["/usr/src/words-gen-api/start.sh"]