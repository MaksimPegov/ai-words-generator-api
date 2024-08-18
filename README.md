# Flask OpenAPI for Word Generation Powered by OpenAI

### Overview

This project is a Flask-based OpenAPI that utilizes OpenAI’s GPT-4 model to generate words based on a user-provided topic. It serves as a simple yet powerful tool for generating word suggestions, making it ideal for creative projects, brainstorming sessions, or content creation.

### Features

- Topic-Based Word Generation: Submit a topic, and the API will return a list of words relevant to that topic.
- Powered by OpenAI: Leverages OpenAI’s GPT-4 model to ensure high-quality, contextually relevant word suggestions.
- RESTful API: Provides easy-to-use API endpoints for seamless integration into other applications.
- 
<hr>

## API Endpoint:
#### Endpoint: /generate
#### Method: POST
#### Request Body:
- topic (string): The topic for which you want to generate words.
#### Response:
- words (list): A list of words generated based on the provided topic.

### Example Request:
```json
{
  "topic": "technology"
}
```
### Example Response

```json
  ["innovation", "software", "AI", "data", "automation"]
```

# Testing the API

You can test the API through its frontend interface available at the following URL:

[API Frontend Interface](https://github.com/MaksimPegov/ai-words-generator-web)
