import os
from dotenv import load_dotenv

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

class LangGraphWrapper:
    def __init__(self):
        self.api_key = os.getenv('LANGGRAPH_API_KEY')

    def execute(self, plan: dict):
        # This is a mock implementation for local dev.
        # Replace with real LangGraph calls when available.
        return {"executed": True, "plan_summary": f"Executed {len(plan.get('steps', []))} steps"}
