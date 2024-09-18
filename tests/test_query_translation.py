import pytest
from backend.query_translator import translate_to_sql

# Mock the NLU response since it's already tested separately
@pytest.mark.parametrize("question, expected_sql", [
    ("How many open tickets are there?", "SELECT COUNT(*) FROM it_tickets WHERE status = 'Open';"),
    ("How many high-priority tickets have been assigned to John Doe?", "SELECT COUNT(*) FROM it_tickets WHERE priority = 'High' AND assigned_to = 'John Doe';"),
])
def test_translate_to_sql(question, expected_sql):
    # Mocking the call to generate_gemini_response (since it's tested elsewhere)
    with pytest.monkeypatch.context() as m:
        m.setattr('backend.query_translator.generate_gemini_response', lambda q, p: expected_sql)
        
        # Call the translation function
        sql_query = translate_to_sql(question)
        
        # Assertions
        assert sql_query == expected_sql
