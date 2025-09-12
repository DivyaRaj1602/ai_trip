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


