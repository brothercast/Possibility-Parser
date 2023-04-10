import json
from flask import Flask, render_template, request, jsonify
import openai
import os
from dotenv import load_dotenv

# Load .env file
load_dotenv()

# Set up ChatGPT API credentials
openai.api_key = os.getenv("OPENAI_API_KEY")

def generate_text(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )

    return response.choices[0].text.strip()

def process_possibility(possibility_text):
    # Use ChatGPT to generate the goal, domain, and conditions
    prompt = f"Given the possibility: '{possibility_text}', generate a goal, a domain, and five conditions of satisfaction:"
    generated_text = generate_text(prompt)

    # Split the generated text into lines
    lines = generated_text.splitlines()

    # Create a dictionary with goal, domain, and conditions
    parsed_output = {
        "goal": lines[0],
        "domain": lines[1],
        "conditions": lines[2:]
    }

    return parsed_output

app = Flask(__name__)

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

@app.route("/parse", methods=["POST"])
def parse_possibility():
    user_input = request.form["possibility"]
    parsed_output = process_possibility(user_input)
    # Assuming parsed_output is a dictionary with the structure: {"goal": "...", "domain": "...", "conditions": [...]}
    return jsonify(parsed_output)

if __name__ == "__main__":
    app.run(debug=True)
