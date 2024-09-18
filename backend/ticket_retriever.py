import sqlite3

def get_tickets(sql_query, db="data/it_tickets_db.sqlite"):
    conn = sqlite3.connect(db)
    cursor = conn.cursor()
    cursor.execute(sql_query)
    results = cursor.fetchall()
    conn.close()
    return results
