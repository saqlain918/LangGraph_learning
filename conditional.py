from typing import TypedDict
from langgraph.graph import StateGraph, END

# Step 1: Define State
class State(TypedDict, total=False):
    user_type: str
    recommendation: str

# Step 2: Define nodes
def get_user_type(state: State):
    """Ask user at runtime"""
    user = input("Are you a student or developer? ").strip().lower()
    if user not in ["student", "developer"]:
        print("⚠️ Invalid input! Defaulting to student.")
        user = "student"
    return {"user_type": user}

def student_recommendation(state: State):
    return {"recommendation": "📚 Study tip: Make a daily schedule and revise regularly."}

def developer_recommendation(state: State):
    return {"recommendation": "💻 Dev tip: Practice coding daily and explore open-source projects."}

# Step 3: Build the graph
graph = StateGraph(State)

graph.add_node("get_user_type", get_user_type)
graph.add_node("student_recommendation", student_recommendation)
graph.add_node("developer_recommendation", developer_recommendation)

graph.set_entry_point("get_user_type")

# Step 4: Conditional branching
def route_user(state: State):
    if state["user_type"] == "student":
        return "student_recommendation"
    else:
        return "developer_recommendation"

graph.add_conditional_edges(
    "get_user_type",
    route_user,
    {
        "student_recommendation": "student_recommendation",
        "developer_recommendation": "developer_recommendation",
    },
)

graph.set_finish_point("student_recommendation")
graph.set_finish_point("developer_recommendation")

# Step 5: Compile and run
app = graph.compile()

print("\n---- Result ----")
print(app.invoke({}))
