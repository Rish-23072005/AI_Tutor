from .mcp_client import MCPClient
from .langgraph_wrapper import LangGraphWrapper

from .parameter_extractor import extract_parameters
from .validator import validate_tool_params, EducationalContextValidator

class Orchestrator:
    def __init__(self):
        self.mcp = MCPClient()
        self.lg = LangGraphWrapper()

    def run(self, prompt: str, teaching_style: str, emotional_state: str, mastery_level: int, tool: str, extra_params: dict):
        # Validate educational context
        EducationalContextValidator.validate(teaching_style, emotional_state, mastery_level)

        # Extract base parameters
        params = extract_parameters(prompt)
        params.update(extra_params)

        # Adapt parameters based on context
        # Example adaptation logic (expand as needed)
        if tool == "note_maker":
            if teaching_style == "Direct":
                params["note_taking_style"] = "outline"
                params["include_examples"] = False
                params["include_analogies"] = False
            elif teaching_style == "Visual":
                params["note_taking_style"] = "structured"
                params["include_examples"] = True
                params["include_analogies"] = True
        if tool == "flashcard_generator":
            if mastery_level <= 3:
                params["difficulty"] = "easy"
            elif mastery_level <= 6:
                params["difficulty"] = "medium"
            else:
                params["difficulty"] = "hard"
        if tool == "concept_explainer":
            if emotional_state == "Confused":
                params["desired_depth"] = "basic"
            elif emotional_state == "Focused":
                params["desired_depth"] = "advanced"

        # Validate tool parameters
        validate_tool_params(tool, params)

        # Invoke MCP (mock) to generate a plan
        plan = self.mcp.create_plan(prompt, params)

        # Optionally send plan to LangGraph wrapper (mock)
        lg_result = self.lg.execute(plan)

        # Simple combined response
        return {
            "prompt": prompt,
            "parameters": params,
            "plan": plan,
            "langgraph": lg_result,
            "context": {
                "teaching_style": teaching_style,
                "emotional_state": emotional_state,
                "mastery_level": mastery_level,
                "tool": tool
            }
        }
