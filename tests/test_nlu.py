import pytest
from unittest.mock import patch
from backend.nlu_module import generate_gemini_response

# Mock test for generate_gemini_response
@patch('backend.nlu_module.genai.GenerativeModel.generate_content')
def test_generate_gemini_response(mock_generate_content):
    # Mock the response of the generative model
    mock_generate_content.return_value = type('obj', (object,), {'text': 'SELECT * FROM it_tickets WHERE status = "Open";'})
    
    # Example question and input prompt
    question = "How many open tickets are there?"
    input_prompt = "You are an expert in converting English questions to SQL code!"
    
    # Call the function
    response = generate_gemini_response(question, input_prompt)
    
    # Assertions
    assert response == 'SELECT * FROM it_tickets WHERE status = "Open";'
    mock_generate_content.assert_called_once()
