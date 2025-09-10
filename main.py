from typing import TypedDict
from langgraph.graph import StateGraph, END

# Step 1: Define State properly
class State(TypedDict, total=False):
    step1: str
    step2: str
    step3: str

# Step 2: Define nodes
def step1(state: State):
    return {"step1": "I cracked the egg."}

def step2(state: State):
    return {"step2": "I fried the egg."}

def step3(state: State):
    return {"step3": "I served the egg."}

# Step 3: Build graph
graph = StateGraph(State)

graph.add_node("step1", step1)
graph.add_node("step2", step2)
graph.add_node("step3", step3)

graph.set_entry_point("step1")
graph.add_edge("step1", "step2")
graph.add_edge("step2", "step3")
graph.set_finish_point("step3")

# Step 4: Compile app
app = graph.compile()

# Step 5: Run it
result = app.invoke({})
print(result)
