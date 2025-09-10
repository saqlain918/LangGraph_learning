from typing import TypedDict
from langgraph.graph import StateGraph

# 1. Define the State (the "backpack")
class State(TypedDict, total=False):
    name: str
    hobby: str
    response: str

# 2. Define Nodes
def ask_name(state: State):
    name = input("👋 Hi! What is your name? ").strip()
    return {"name": name}

def ask_hobby(state: State):
    hobby = input(f"😊 Nice to meet you {state['name']}! What's your favorite hobby? ").strip()
    return {"hobby": hobby}

def final_response(state: State):
    message = f"🎉 Great! So your name is {state['name']} and you enjoy {state['hobby']}."
    return {"response": message}

# 3. Build the Graph
graph = StateGraph(State)

graph.add_node("ask_name", ask_name)
graph.add_node("ask_hobby", ask_hobby)
graph.add_node("final_response", final_response)

graph.set_entry_point("ask_name")
graph.add_edge("ask_name", "ask_hobby")
graph.add_edge("ask_hobby", "final_response")
graph.set_finish_point("final_response")

# 4. Compile & Run
app = graph.compile()

print("\n🤖 Starting mini agent...\n")
result = app.invoke({})
print("\n✨ --- Conversation Result ---")
print(result["response"])
