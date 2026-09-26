from typing import TypedDict
import os

MOCK_LLM = os.getenv("MOCK_LLM", "1")

class State(TypedDict):
    query: str
    intent: str
    context: str
    answer: str

def classify_intent(state: State) -> State:
    q = state["query"].lower()
    if "policy" in q or "refund" in q or "delivery" in q:
        state["intent"] = "policy_question"
    else:
        state["intent"] = "general_question"
    return state

def retrieve_context(state: State) -> State:
    if state["intent"] == "policy_question":
        # In real mode, query ChromaDB; here we mock
        state["context"] = "Relevant Zepto policy text."
    else:
        state["context"] = ""
    return state

def generate_answer(state: State) -> State:
    if MOCK_LLM == "1":
        # Deterministic mock answer
        if state["intent"] == "policy_question":
            state["answer"] = f"Based on Zepto policy: {state['context']}"
        else:
            state["answer"] = "This is a general answer (mock mode)."
    else:
        # Real LLM call (optional extension)
        state["answer"] = "Real LLM response here."
    return state

def run_flow(query: str) -> dict:
    state: State = {"query": query, "intent": "", "context": "", "answer": ""}
    state = classify_intent(state)
    state = retrieve_context(state)
    state = generate_answer(state)
    return state
