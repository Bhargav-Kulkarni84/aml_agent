from enum import Enum
from typing import Any

from pydantic import BaseModel, Field


class Tool(str, Enum):
    EDA = "EDA"
    FEATURE = "FEATURE"
    ANOMALY = "ANOMALY"
    RISK = "RISK"
    EXPLANATION = "EXPLANATION"


class ToolStep(BaseModel):
    tool: Tool
    reason: str


class ExecutionPlan(BaseModel):
    intent: str = Field(
        description="Detected user intent"
    )

    filters: dict[str, Any] = Field(
        default_factory=dict
    )

    steps: list[ToolStep]