from google import genai
from google.genai import types

from src.agent.prompt import PLANNER_PROMPT
from src.agent.schemas import ExecutionPlan
from src.config import GEMINI_API_KEY


class LLMPlanner:

    def __init__(self):

        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def plan(self, query: str) -> ExecutionPlan:

        response = self.client.models.generate_content(
            model="gemini-2.5-flash",

            contents=f"""
            {PLANNER_PROMPT}

            User Query:

            {query}
            """,

            config=types.GenerateContentConfig(
                response_mime_type="application/json",
                response_schema=ExecutionPlan,
                temperature=0
            )
        )

        return response.parsed