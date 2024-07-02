import os
from dotenv import dotenv_values
import base64

from flask import Flask
from flask import request

import vertexai
from vertexai.generative_models import GenerativeModel, Part, FinishReason
import vertexai.preview.generative_models as generative_models

app = Flask(__name__)
SECRETS = dotenv_values(".env")

@app.route("/")
def hello_world():
    """Example Hello World route."""
    name = os.environ.get("NAME", "World")
    return f"Hello {name}!"

@app.route("/generate", methods=["GET"])  # Allow GET requests
def generate_text():
    """Generate text based on a 'prompt' argument passed in the URL."""

    prompt = request.args.get("prompt")

    if prompt is None:
        return "Error: Missing 'prompt' parameter", 400  # Bad Request

    # Call the generate() function with the prompt
    generated_text = generate(system_message="Answer the following question with a quirky pirate accent:", prompt=prompt)  # Assuming you have a function called 'generate' defined elsewhere

    # Return the generated text with a 200 status code
    return generated_text, 200

def generate(system_message, prompt):
  vertexai.init(project=SECRETS["GCP_PROJECT_ID"], location=SECRETS["GCP_REGION"])
  
  generation_config = {
        "max_output_tokens": 8192,
        "temperature": 1,
        "top_p": 0.95,
    }

  model = GenerativeModel(
    "gemini-1.5-flash-001",
    system_instruction=[system_message]
  )
  
  response = model.generate_content(
      [prompt],
      generation_config=generation_config,
  )

  return response.text



if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))

    # response = generate(system_message="Answer the following question with a quirky pirate accent:", prompt="What is the meaning of life?")
    # print(response)