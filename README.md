## LangGraph Learning Journey

This repository contains my step-by-step practice with LangGraph, a framework for building LLM-powered workflows using graph structures with nodes, edges, and state management. Each file demonstrates different LangGraph concepts and implementations.

## What it does

- Demonstrates LangGraph fundamentals through practical examples
- Shows how to build workflows using graph structures (nodes, edges, state)
- Explores different patterns: simple graphs, multi-node chains, conditionals, and LLM integration
- Implements state management and memory across conversation turns
- Combines LLMs with external tools for enhanced functionality
- Provides human-in-the-loop control mechanisms

## What I Learned

### 1. Graph Basics
- **Node:** A step or function in the workflow
- **Edge:** Connection that defines flow between nodes
- **State:** Data passed across nodes for memory and context

**Example Flow:**
```
step1 → step2 → step3 (like a cooking recipe)
```

### 2. Multi-Node Graphs
- Multiple nodes chained together for complex workflows
- **Example:** User Input → Greeting → Closing message

### 3. Conditionals & Branching
- Use `add_conditional_edges` for if/else logic flows
- **Example:**
  - If user is student → recommend study tips
  - If user is developer → recommend coding tips

### 4. LLM Integration
- Added LLM (Gemini) node for dynamic responses
- **Flow:** Input → LLM → Output
- Can mix tools (calculator, search API, databases)
- **Rule of thumb:**
  - LLM → reasoning, text generation
  - Tool → factual/external info (math, API, DB)

### 5. State Management
- State keeps memory across conversation turns
- **Without memory:** Bot forgets previous messages
- **With memory:** Bot recalls history, name, preferences

### 6. Customized State
- **Default state:** Simple dictionary
- **Custom state:** Structured model (Pydantic or TypedDict)

**Benefits:**
- Validation (user_input must be string)
- Defaults (history = [])
- Merge rules (append vs replace)

**Example:**
```python
class State(BaseModel):
    user_input: str = ""
    response: str = ""
    history: List[str] = Field(default_factory=list)
```

**Result:**
```
👤 You: hi
🤖 Bot: I heard you say 'hi'
🧾 Conversation so far: ["hi"]
```

## Project Structure

```
langgraph-learning/
├── main.py                          # First LangGraph test (simple single-node)
├── greetings.py                     # Multi-node graph workflow
├── conditional.py                   # Branching and conditional logic
├── LLM.py                          # LLM integration with Gemini
├── tools.py                        # LLM + external tools combination
├── state.py                        # Graph state and memory management
├── Multi-turn Conversational.py    # Chatbot with conversation memory
├── customize.py                    # Custom state with Pydantic
├── human.py                        # Human-in-the-loop control
└── README.txt                      # Project documentation
```

## Files Overview

### 1. main.py
- First LangGraph test with simple single-node graph
- Example: One node prints a greeting

### 2. greetings.py
- Multi-node graph demonstration
- Flow: User input → Greeting → Closing message

### 3. conditional.py
- Demonstrates branching logic
- If user_type = student → study tips
- If user_type = developer → coding resources

### 4. LLM.py
- Integrates LLM (Gemini) into workflow
- Flow: Input → LLM response → Output

### 5. tools.py
- Shows combining LLM with external tools
- Example: Calculator or external API usage

### 6. state.py
- Explains graph state and memory management
- Passes user data across multiple nodes

### 7. Multi-turn Conversational.py
- Mini chatbot with memory across turns
- Keeps track of conversation history

### 8. customize.py
- Demonstrates custom state with Pydantic
- Structured memory and validation

### 9. human.py
- Human-in-the-loop control implementation
- Adds pause step for manual review before continuing

## How to use

1. Clone the repository and navigate to the project folder

2. Install required dependencies:
   ```
   pip install langgraph langchain pydantic
   ```

3. Run individual examples:
   ```
   python main.py           # Basic graph
   python greetings.py      # Multi-node workflow
   python conditional.py    # Conditional branching
   python LLM.py           # LLM integration
   ```

4. Each file demonstrates a specific LangGraph concept and can be run independently

## Requirements

- Python 3.10+
- LangGraph
- LangChain
- Pydantic
- Google Gemini API key (for LLM examples)

## Key Concepts

**Graph Structure:** Nodes connected by edges with shared state

**State Management:** Memory that persists across workflow steps

**Conditional Logic:** Branching paths based on conditions

**LLM Integration:** AI-powered reasoning and text generation

**Tool Integration:** External APIs and services

**Human-in-the-Loop:** Manual intervention points in automated workflows

## Use Cases

- Building conversational AI agents
- Creating complex workflow automation
- Implementing decision trees with AI
- Developing multi-step reasoning systems
- Creating interactive applications with memory

## Next Steps

- Explore merge strategies for better memory management
- Add LangSmith tracing for debugging and monitoring
- Build complete chatbot agent with LLM + tools
- Implement more complex conditional workflows
- Add persistence for long-term memory

## Key Takeaway

**LangChain:** AI building blocks and components
**LangGraph:** Orchestrates and manages workflows
**LangSmith:** Debugs and monitors applications

**Development Flow:**
Build with LangChain → Orchestrate with LangGraph → Debug with LangSmith

## Built with

- Python
- LangGraph
- LangChain
- Pydantic
- Google Gemini API

## Notes

- Each file is self-contained and demonstrates specific concepts
- Examples progress from simple to complex implementations
- Focus on practical learning through hands-on coding
- Structured approach to understanding LangGraph ecosystem
