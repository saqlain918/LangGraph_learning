from typing import TypedDict
from langgraph.graph import StateGraph
from langchain_google_genai import ChatGoogleGenerativeAI
import os

# 1. Set your Gemini API key
os.environ["GOOGLE_API_KEY"] = ""

# 2. Define State
class State(TypedDict, total=False):
    user_input: str
    llm_response: str

# 3. Create LLM
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")

# 4. Define nodes
def get_input(state: State):
    return {"user_input": state["user_input"]}

def generate_response(state: State):
    response = llm.invoke(state["user_input"])
    return {"llm_response": response.content}

# 5. Build graph
graph = StateGraph(State)
graph.add_node("get_input", get_input)
graph.add_node("generate_response", generate_response)

graph.set_entry_point("get_input")
graph.add_edge("get_input", "generate_response")
graph.set_finish_point("generate_response")

app = graph.compile()

# 6. Run interactively
user_text = input("💬 Ask Gemini anything: ")
result = app.invoke({"user_input": user_text})

# 7. Pretty output
print("\n✨ --- Gemini Response --- ✨")
print(f"🧑 You: {result['user_input']}")
print(f"🤖 Gemini: {result['llm_response']}")
print("✨ ------------------------ ✨")
