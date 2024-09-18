from fastapi import FastAPI
from pydantic import BaseModel
from backend.query_translator import translate_to_sql
from backend.ticket_retriever import get_tickets

app = FastAPI()

class QueryRequest(BaseModel):
    question: str
    refined_sql: str = None

@app.post("/process_query/")
def process_query(query_request: QueryRequest):
    question = query_request.question


    if query_request.refined_sql:
        sql_query = query_request.refined_sql
    else:
        sql_query = translate_to_sql(question)
    tickets = get_tickets(sql_query)
    return {"query": sql_query, "results": tickets}
