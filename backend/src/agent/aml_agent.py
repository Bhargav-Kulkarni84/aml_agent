from src.tools.eda_tool import EDATool
from src.tools.feature_tool import FeatureTool
from src.tools.anamoly_tool import AnomalyTool
from src.tools.risk_tool import RiskTool
from src.tools.explanation_tool import ExplanationTool
from src.agent.llm_planner import LLMPlanner
from src.agent.schemas import Tool

class AMLAgent:

    def __init__(self):

        self.planner = LLMPlanner()

        self.tools = {
            Tool.EDA: EDATool(),
            Tool.FEATURE: FeatureTool(),
            Tool.ANOMALY: AnomalyTool(),
            Tool.RISK: RiskTool(),
            Tool.EXPLANATION: ExplanationTool()
        }

    def handle_query(self,query,df):
        
        plan = self.planner.plan(query)

        context = {
            "data": df,
            "query": query,
            "plan": plan
        }

        print("\nEXECUTION PLAN")
        print(f"Intent: {plan.intent}")
        print(f"Confidence: {plan.confidence:.2f}")

        for step in plan.steps: 
            print(f"{step.tool.value}: {step.reason}")

        # for step in plan.steps:

        #     print(f"\nRunning {step.tool.value}")
        #     tool = self.tools[step.tool]
        #     context = tool.run(context)
        #     print(f"{step.tool.value} completed")

        for step in plan.steps:

            print(f"\n========== {step.tool.value} ==========")

            tool = self.tools[step.tool]

            try:
                context = tool.run(context)
                print(f"{step.tool.value} completed successfully")

            except Exception as e:
                print(f"{step.tool.value} FAILED")
                raise e

        return context