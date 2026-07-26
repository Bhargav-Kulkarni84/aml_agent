class RiskTool:

    def run(self, context):

        probability = context["probability"]

        risk = []

        for p in probability:

            if p < 0.30:
                risk.append("Low")

            elif p < 0.70:
                risk.append("Medium")

            else:
                risk.append("High")

        context["risk"] = risk

        return context