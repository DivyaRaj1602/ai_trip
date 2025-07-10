Key Features:
Free-form Query Support: Accepts natural language queries like “Plan a 7-day trip to Manali under ₹30,000 with good weather” and returns a detailed plan.

Tool-Aware Agent: Uses LangGraph to build a looping state machine where the agent decides whether to call a tool or proceed with response generation.

Graphical Execution Flow: Each LLM interaction is visualized as a Mermaid flowchart PNG to trace decision points and tool usage in real time.

Real-World APIs Integration:

🗺️ Google Places, Foursquare for POIs and activities

🌤️ OpenWeatherMap for weather forecasts

💱 ExchangeRate API for currency conversion

🧮 Custom calculator for budget and expense breakdown

Modular, Extensible Architecture: Tools are imported as modular classes, supporting clean separation of logic and easy extensibility.

Technical Architecture:
🔹 LangGraph Workflow Agent:
State machine-based design using langgraph.StateGraph

Nodes:

agent: handles LLM prompt/response

tools: conditionally invoked if tool use is triggered

Conditional branching via tools_condition() to decide tool use dynamically

🔹 Agent Function Logic:
Prompts built using SYSTEM_PROMPT + user message

Tools bound to LLM using .bind_tools(tools=...)

LangChain invoke() used to send messages and receive structured tool calls

Final response returned as part of the message state

🔹 Backend (FastAPI):
/query endpoint receives user query

Loads and compiles agent graph, invokes agent, and returns the last AI message

Graph PNG exported and saved for each interaction (via .draw_mermaid_png())

🔹 Frontend (Streamlit):
User-friendly UI to enter travel prompts

POSTs to FastAPI endpoint and renders AI response in Markdown

Includes metadata like date, signature, and disclaimers

🔹 Deployment:
Backend: Hosted on Render, configured with dynamic port binding and environment variables for API keys.

Frontend: Hosted on Streamlit Cloud using the same repo, auto-connected to the deployed backend.
