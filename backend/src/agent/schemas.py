from enum import Enum
from typing import Any

from pydantic import BaseModel, Field

class Tool(str, Enum):
    EDA = "EDA"
    FEATURE = "FEATURE"
    ANOMALY = "ANOMALY"
    RISK = "RISK"
    EXPLANATION = "EXPLANATION"
    REPORT = "REPORT"


class ToolStep(BaseModel):
    tool: Tool
    reason: str


class ExecutionPlan(BaseModel):
    intent: str = Field(description="Detected user intent")
    confidence: float = Field(description="Confidence between 0 and 1.")
    steps: list[ToolStep]