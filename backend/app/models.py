from pydantic import BaseModel
from typing import Dict

class PlanStep(BaseModel):
    step: int
    action: str
    detail: Dict | str | None = None

class Plan(BaseModel):
    steps: list[PlanStep]
