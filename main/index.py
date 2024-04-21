from flask import Flask, jsonify, request
from flask_cors import CORS
from openai import OpenAI

app = Flask(__name__)
CORS(app)
client = OpenAI()

def read_file(file_path):
    with open(file_path, 'r') as file:
        content = file.read()
    return content

prompt_file_path = 'main/system-context.txt'

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

    words = message.replace(' ', '').replace('.', '').split(',')
    return jsonify(words), 200

@app.route('/test', methods=['POST'])
def test():
    return jsonify("All is up and running!"), 200
