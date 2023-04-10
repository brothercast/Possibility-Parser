# SSPEC Possibility Parser Engine

## Overview
The SSPEC Possibility Parser Engine is a web application that uses OpenAI's GPT-3 to generate a goal, domain, and conditions of satisfaction given a possibility. The goal, domain, and conditions are presented in a slot-machine-style interface.

## Getting Started
To use the SSPEC Possibility Parser Engine, simply enter a possibility into the input field and click the "Parse" button. The parsed output will be displayed in the slot-machine-style interface below.

## Dependencies
- Flask
- Spacy
- OpenAI

## Installation
To install the SSPEC Possibility Parser Engine, follow these steps:

1. Clone the repository
2. Install the required dependencies by running `pip install -r requirements.txt`
3. Set up your OpenAI API credentials by setting the `OPENAI_API_KEY` environment variable.

## Usage
To run the SSPEC Possibility Parser Engine, execute the following command in the project directory:
python app.py

The web application will be accessible at `http://localhost:5000`.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
- OpenAI
- Bootstrap
- jQuery