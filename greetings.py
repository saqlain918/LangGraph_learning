from typing import TypedDict
from langgraph.graph import StateGraph, END

# Step 1: Define the State (the backpack 🎒)
class State(TypedDict, total=False):
    name: str
    greeting: str
    closing: str

# Step 2: Define nodes (functions)

def get_name(state: State):
    """Simulates user input"""
    return {"name": "Ali"}   # you can replace with input()

def greet(state: State):
    """Create a greeting using the name"""
    return {"greeting": f"Hello {state['name']}! How are you today?"}

def closing(state: State):
    """Closing message"""
    return {"closing": f"It was nice chatting, {state['name']}. Goodbye!"}

# Step 3: Build the graph
graph = StateGraph(State)

graph.add_node("get_name", get_name)
graph.add_node("greet", greet)
graph.add_node("closing", closing)

# Step 4: Connect nodes with edges
graph.set_entry_point("get_name")    # Start here
graph.add_edge("get_name", "greet")  # After name → greet
graph.add_edge("greet", "closing")   # After greeting → closing
graph.set_finish_point("closing")    # End here

# Step 5: Compile and run
app = graph.compile()
result = app.invoke({})
print(result)
