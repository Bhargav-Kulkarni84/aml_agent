class RiskTool:

    def classify(self, probability):

        if probability < 0.30: return "Low"
        elif probability < 0.70: return "Medium"
        return "High"