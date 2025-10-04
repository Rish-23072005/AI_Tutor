from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .orchestrator import Orchestrator
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

app = FastAPI(title="AI Tutor Orchestrator (backend)")


class ContextRequest(BaseModel):
    prompt: str
    teaching_style: str
    emotional_state: str
    mastery_level: int
    tool: str  # 'note_maker', 'flashcard_generator', 'concept_explainer'
    extra_params: dict = {}

orch = Orchestrator()

@app.get("/health")
def health():
    return {"status":"ok"}


@app.post("/orchestrate")
def orchestrate(req: ContextRequest):
    try:
        result = orch.run(
            prompt=req.prompt,
            teaching_style=req.teaching_style,
            emotional_state=req.emotional_state,
            mastery_level=req.mastery_level,
            tool=req.tool,
            extra_params=req.extra_params
        )
        return {"ok": True, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
