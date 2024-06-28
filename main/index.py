from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

prompt_file_path = 'main/system-context.txt'

app = Flask(__name__)
client = OpenAI()
CORS(app)

@app.route('/generate', methods=['POST'])
def generate():
    # request = {"topic": "user topic here"}
    topic = request.get_json().get('topic')

    completion = client.chat.completions.create(
      model="gpt-3.5-turbo",
      messages=[
        {"role": "system", "content": read_file(prompt_file_path)},
        {"role": "user", "content": topic},
      ],
      max_tokens=150
    )

    message = completion.choices[0].message.to_dict().get('content')

    print(message)

    if "FAIL" in message:
        return jsonify(message.replace("FAIL:",'').strip()), 400
    
    if "SUCCESS" in message:
        words = message.replace("SUCCESS:",'').replace(' ', '').replace('.', '').split(',')
        return jsonify(words), 200
    
    return jsonify('Something went wrong, try again.'), 500



@app.route('/test', methods=['POST'])
def test():
    return jsonify("All is up and running!"), 200
