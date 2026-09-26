from fastapi import FastAPI
from langgraph_flow import run_flow

app = FastAPI()

@app.get("/ask")
def ask(query: str):
    return run_flow(query)
