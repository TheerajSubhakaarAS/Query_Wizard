import google.generativeai as genai
import json


with open('backend/config.json') as f:
    config = json.load(f)


api_key = config.get('Generative_Language_Client')
genai.configure(api_key=api_key)

def generate_gemini_response(question, input_prompt):
    response = genai.GenerativeModel(model_name="gemini-pro").generate_content([input_prompt, question])
    return response.text.strip()
