from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from .orchestrator import Orchestrator
from dotenv import load_dotenv
import os

load_dotenv(dotenv_path=os.path.join(os.path.dirname(__file__), "..", ".env"))

app = FastAPI(title="AI Tutor Orchestrator (backend)")

class RequestIn(BaseModel):
    prompt: str

orch = Orchestrator()

@app.get("/health")
def health():
    return {"status":"ok"}

@app.post("/orchestrate")
def orchestrate(req: RequestIn):
    try:
        result = orch.run(req.prompt)
        return {"ok": True, "result": result}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))
