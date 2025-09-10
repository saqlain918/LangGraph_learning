from typing import TypedDict
from langgraph.graph import StateGraph, END
from langchain_google_genai import ChatGoogleGenerativeAI

# 🔑 API Key inline
GEMINI_API_KEY = ""
llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash", api_key=GEMINI_API_KEY)


# --- State ---
class State(TypedDict, total=False):
    user_input: str
    approved_text: str


# --- Nodes ---
def get_user_input(state: State):
    msg = input("👤 You (what should the email be about?): ")
    return {"user_input": msg}


def draft_and_review(state: State):
    """LLM drafts an email + Human reviews immediately"""
    topic = state["user_input"]
    draft = llm.invoke(f"Write a short professional email about: {topic}").content

    print("\n✉️ Draft Email:")
    print(draft)

    # Human review step
    new_text = input("✏️ Edit draft or press Enter to approve: ").strip()
    if new_text == "":
        approved = draft
    else:
        approved = new_text

    return {"approved_text": approved}


def send_email(state: State):
    print("\n📤 Email Sent:")
    print(state["approved_text"])
    return {}


# --- Graph ---
graph = StateGraph(State)
graph.add_node("get_user_input", get_user_input)
graph.add_node("draft_and_review", draft_and_review)
graph.add_node("send_email", send_email)

graph.set_entry_point("get_user_input")
graph.add_edge("get_user_input", "draft_and_review")
graph.add_edge("draft_and_review", "send_email")
graph.set_finish_point("send_email")

app = graph.compile()

# --- Run ---
app.invoke({})
