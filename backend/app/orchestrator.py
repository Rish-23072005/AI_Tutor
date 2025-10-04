from .mcp_client import MCPClient
from .langgraph_wrapper import LangGraphWrapper
from .parameter_extractor import extract_parameters
from .validator import validate_prompt

class Orchestrator:
    def __init__(self):
        self.mcp = MCPClient()
        self.lg = LangGraphWrapper()

    def run(self, prompt: str):
        # Basic validation
        validate_prompt(prompt)

        # Extract parameters (very simple)
        params = extract_parameters(prompt)

        # Invoke MCP (mock) to generate a plan
        plan = self.mcp.create_plan(prompt, params)

        # Optionally send plan to LangGraph wrapper (mock)
        lg_result = self.lg.execute(plan)

        # Simple combined response
        return {
            "prompt": prompt,
            "parameters": params,
            "plan": plan,
            "langgraph": lg_result
        }
