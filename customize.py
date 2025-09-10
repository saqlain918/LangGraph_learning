from pydantic import BaseModel, Field
from typing import List
from langgraph.graph import StateGraph, END

# --- Step 1: Define State ---
class State(BaseModel):
    user_input: str = ""
    response: str = ""
    history: List[str] = Field(default_factory=list)

# --- Step 2: Define Nodes ---
def get_user_input(state: State):
    msg = input("👤 You: ")
    return {"user_input": msg}

def bot_response(state: State):
    user_msg = state.user_input
    reply = f"🤖 Bot: I heard you say '{user_msg}'"
    return {
        "response": reply,
        "history": state.history + [reply]   # ✅ append, not replace
    }

def show_response(state: State):
    print(state.response)
    return {}

# --- Step 3: Build Graph ---
graph = StateGraph(State)

graph.add_node("get_user_input", get_user_input)
graph.add_node("bot_response", bot_response)
graph.add_node("show_response", show_response)

graph.set_entry_point("get_user_input")
graph.add_edge("get_user_input", "bot_response")
graph.add_edge("bot_response", "show_response")
graph.set_finish_point("show_response")

app = graph.compile()

# --- Step 4: Run Loop ---
state = State().model_dump()   # dict to start with

while True:
    state = app.invoke(state)
    if state["user_input"].lower() in ["bye", "exit", "quit"]:
        print("👋 Goodbye!")
        break

    print("🧾 Conversation so far:", state["history"])
