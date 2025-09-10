from typing import TypedDict, List
from langgraph.graph import StateGraph
from langchain_google_genai import ChatGoogleGenerativeAI
import re

# 🔑 API Key inline (replace with your real key)
GEMINI_API_KEY = ""

# Initialize Gemini LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=GEMINI_API_KEY)

# --- State ---
class State(TypedDict, total=False):
    history: List[str]
    user_input: str
    response: str

# --- Nodes ---
def get_user_input(state: State):
    user_msg = input("👤 You: ").strip()
    return {"user_input": user_msg}

def decide_route(state: State):
    user_msg = state["user_input"]
    if re.fullmatch(r"\d+\s*[\+\-\*/]\s*\d+", user_msg):
        return "calculator"
    elif user_msg.lower() == "bye":
        return "goodbye"
    return "llm_response"

def llm_response(state: State):
    user_msg = state["user_input"]
    ai_msg = llm.invoke(user_msg).content
    print(f"🤖 Bot: {ai_msg}")   # ✅ print here directly
    history = state.get("history", [])
    history.append(f"👤 You: {user_msg}")
    history.append(f"🤖 Bot: {ai_msg}")
    return {"response": ai_msg, "history": history}

def calculator(state: State):
    expr = state["user_input"]
    try:
        result = eval(expr)
        bot_msg = f"🧮 The result of {expr} is {result}"
    except Exception:
        bot_msg = "⚠️ Sorry, I couldn't calculate that."
    print(f"🤖 Bot: {bot_msg}")   # ✅ print here directly
    history = state.get("history", [])
    history.append(f"👤 You: {expr}")
    history.append(f"🤖 Bot: {bot_msg}")
    return {"response": bot_msg, "history": history}

def goodbye(state: State):
    bot_msg = "👋 Goodbye!"
    print(f"🤖 Bot: {bot_msg}")   # ✅ print here directly
    history = state.get("history", [])
    history.append(f"👤 You: {state['user_input']}")
    history.append(f"🤖 Bot: {bot_msg}")
    return {"response": bot_msg, "history": history}

# --- Graph ---
graph = StateGraph(State)

graph.add_node("get_user_input", get_user_input)
graph.add_node("llm_response", llm_response)
graph.add_node("calculator", calculator)
graph.add_node("goodbye", goodbye)

graph.set_entry_point("get_user_input")

graph.add_conditional_edges(
    "get_user_input",
    decide_route,
    {
        "llm_response": "llm_response",
        "calculator": "calculator",
        "goodbye": "goodbye"
    }
)

graph.add_edge("llm_response", "get_user_input")
graph.add_edge("calculator", "get_user_input")

app = graph.compile()

# --- Run ---
print("\n🤖 Hybrid Chatbot (Gemini + Calculator) ready! Type 'bye' to exit.\n")

state = {"history": []}

while True:
    new_state = app.invoke(state)
    state.update(new_state)
    if state.get("user_input", "").lower() == "bye":
        break

# Show history
print("\n✨ --- Conversation History ---")
for turn in state["history"]:
    print(turn)
