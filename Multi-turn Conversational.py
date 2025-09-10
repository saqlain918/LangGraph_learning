from typing import TypedDict, List
from langgraph.graph import StateGraph

# 1. Define the State
class State(TypedDict, total=False):
    history: List[str]
    user_input: str
    response: str

# 2. Define Nodes
def get_user_input(state: State):
    user_msg = input("👤 You: ").strip()
    return {"user_input": user_msg}

def chatbot_response(state: State):
    user_msg = state["user_input"]

    # simple rule-based responses
    if "name" in user_msg.lower():
        bot_msg = "🤖 I'm your friendly LangGraph bot!"
    elif "hobby" in user_msg.lower():
        bot_msg = "🤖 I like helping people build AI workflows 😄"
    elif "bye" in user_msg.lower():
        bot_msg = "👋 Goodbye! Nice chatting with you."
    else:
        bot_msg = f"🤖 You said: {user_msg}"

    # update conversation history
    history = state.get("history", [])
    history.append(f"You: {user_msg}")
    history.append(f"Bot: {bot_msg}")

    return {"response": bot_msg, "history": history}

# 3. Build Graph (no loop edge this time!)
graph = StateGraph(State)

graph.add_node("get_user_input", get_user_input)
graph.add_node("chatbot_response", chatbot_response)

graph.set_entry_point("get_user_input")
graph.add_edge("get_user_input", "chatbot_response")
graph.set_finish_point("chatbot_response")

# 4. Compile
app = graph.compile()

# 5. Run Chat
print("\n🤖 Chatbot ready! Type 'bye' to exit.\n")
state = {"history": []}

while True:
    # one full cycle = ask → respond
    state = app.invoke(state)
    print(state["response"])
    if "bye" in state["user_input"].lower():
        break

print("\n✨ --- Conversation History ---")
for turn in state["history"]:
    print(turn)
