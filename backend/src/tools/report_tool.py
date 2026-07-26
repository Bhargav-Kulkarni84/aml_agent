import json
from google import genai
from src.config import GEMINI_API_KEY

class ReportTool:

    def __init__(self):

        self.client = genai.Client(api_key=GEMINI_API_KEY)

    def run(self, context):

        reports = sorted(
            context.get("reports", []),
            key=lambda x: x["probability"],
            reverse=True
        )

        top_alerts = []

        for report in reports[:5]:

            top_alerts.append({

                "risk": report["risk"],

                "confidence": round(report["probability"] * 100, 2),

                "amount": report["amount"],

                "reasons": report["reasons"]

            })

        summary = {

            "transactions_analyzed": len(context["feature_df"]),

            "flagged_transactions": len(reports),

            "high_risk_transactions": sum(
                1 for r in reports
                if r["risk"] == "High"
            ),

            "top_alerts": top_alerts
        }

        summary = {
            "transactions_analyzed": len(context["feature_df"]),
            "flagged_transactions": len(reports),
            "high_risk_transactions": sum(
                1 for r in reports
                if r["risk"] == "High"
            ),
            "top_alerts": reports[:5]
        }

        prompt = f"""
            You are a Senior Anti-Money Laundering (AML) Investigator working for an international financial institution.

            The AML detection engine has already analyzed the transactions and produced structured findings.

            Your job is NOT to detect suspicious activity again.
            Your job is ONLY to produce a professional investigation report based on the supplied information.

            User Request:
            {context["query"]}

            Generate a concise report (maximum 300 words) with the following sections:

            # Executive Summary
            Summarize the investigation in 2-3 sentences.

            # Overall Risk Assessment
            Describe the overall risk level using the supplied statistics.

            # Key Findings
            Provide concise bullet points highlighting the most important suspicious behaviours.

            # Possible AML Typologies
            Mention only typologies that are supported by the supplied evidence, such as:
            - Structuring
            - Layering
            - Mule Activity
            - Cross-border laundering
            - Rapid movement of funds
            - Currency conversion

            If the evidence does not support a typology, do not mention it.

            # Recommended Actions
            Suggest appropriate investigator actions such as:
            - Enhanced Due Diligence (EDD)
            - Manual review
            - Customer KYC verification
            - Ongoing monitoring
            - Escalation to compliance

            Rules:
            - Use ONLY the supplied JSON.
            - Do NOT invent facts.
            - Do NOT repeat every transaction individually.
            - Summarize repeated behaviour.
            - Convert probabilities into percentages.
            - Refer to accounts as "Account ending XXXX" instead of displaying full account numbers.

            Investigation Data:

            {json.dumps(summary, indent=2)}
            """
        
        response = self.client.models.generate_content(
            model="gemini-3.6-flash",
            contents=prompt
        )

        context["summary"] = summary
        context["llm_report"] = response.text

        return context