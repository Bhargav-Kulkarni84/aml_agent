import json
import google.generativeai as genai


class ReportTool:

    def __init__(self):

        genai.configure(api_key="YOUR_GEMINI_API_KEY")

        self.model = genai.GenerativeModel("gemini-2.5-flash")

    def run(self, context):

        reports = context.get("reports", [])

        summary = {

            "transactions_analyzed": len(context["feature_df"]),

            "flagged_transactions": len(reports),

            "high_risk_transactions":

                sum(
                    1
                    for r in reports
                    if r["risk"] == "High"
                ),

            "top_alerts": reports[:5]

        }

        prompt = f"""
                You are an Anti-Money Laundering Investigation Assistant.

                The AML detection engine has already analyzed the transactions.

                Your task is ONLY to summarize the findings.

                Generate a professional report with the following sections:

                1. Executive Summary

                2. Overall Risk Assessment

                3. Top Suspicious Findings

                4. Recommended Actions

                Use ONLY the supplied JSON.

                Do not invent facts.

                JSON:

        {json.dumps(summary, indent=2)}
        """

        response = self.model.generate_content(prompt)

        context["llm_report"] = response.text

        context["summary"] = summary

        return context