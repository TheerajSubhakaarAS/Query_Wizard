import sqlite3
import pytest
from backend.ticket_retriever import get_tickets

# Setup a test SQLite database for the test
@pytest.fixture(scope='module')
def setup_test_db():
    conn = sqlite3.connect(":memory:")  # Create an in-memory SQLite database
    cursor = conn.cursor()

    # Create a mock it_tickets table
    cursor.execute('''
        CREATE TABLE it_tickets (
            ticket_id INTEGER PRIMARY KEY,
            date_opened TEXT,
            issue_type TEXT,
            priority TEXT,
            assigned_to TEXT,
            status TEXT,
            date_closed TEXT,
            department TEXT,
            description TEXT
        )
    ''')

    # Insert mock data
    cursor.execute("INSERT INTO it_tickets (ticket_id, date_opened, issue_type, priority, assigned_to, status, date_closed, department, description) VALUES (1, '2024-01-10', 'Bug', 'High', 'John Doe', 'Open', NULL, 'IT', 'System crash')")
    cursor.execute("INSERT INTO it_tickets (ticket_id, date_opened, issue_type, priority, assigned_to, status, date_closed, department, description) VALUES (2, '2024-01-11', 'Feature', 'Low', 'Jane Doe', 'Closed', '2024-01-15', 'Finance', 'New dashboard')")
    
    conn.commit()
    yield conn

    # Teardown the database
    conn.close()

def test_get_tickets_open_status(setup_test_db):
    # Test retrieving open tickets
    sql_query = "SELECT * FROM it_tickets WHERE status = 'Open';"
    results = get_tickets(sql_query, db=":memory:")  # Use in-memory DB
    assert len(results) == 1  # We expect one open ticket
    assert results[0][4] == 'John Doe'  # Check that the assigned person is correct

def test_get_tickets_closed_status(setup_test_db):
    # Test retrieving closed tickets
    sql_query = "SELECT * FROM it_tickets WHERE status = 'Closed';"
    results = get_tickets(sql_query, db=":memory:")
    assert len(results) == 1  # We expect one closed ticket
    assert results[0][4] == 'Jane Doe'  # Check that the assigned person is correct
