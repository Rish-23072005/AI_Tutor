from fastapi import FastAPI
from pydantic import BaseModel
from typing import Dict

app = FastAPI(title='MCP Mock Server')

class MCPRequest(BaseModel):
    prompt: str
    params: Dict = {}

@app.post('/mcp/process')
def process(req: MCPRequest):
    # Very simple mock: return a dumb plan based on prompt
    plan = {
        "steps": [
            {"step": 1, "action": "analyze_context", "detail": req.prompt[:120]},
            {"step": 2, "action": "generate_solution_outline", "detail": f"Use language={req.params.get('language')}"},
            {"step": 3, "action": "produce_final_answer"}
        ]
    }
    return {"ok": True, "plan": plan}
