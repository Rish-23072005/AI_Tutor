from pydantic import BaseModel

class OrchestratorResponse(BaseModel):
    prompt: str
    parameters: dict
    plan: dict
    langgraph: dict
