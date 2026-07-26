class ExplanationTool:

    def run(self,row,probability,risk):

        reasons = []

        if row.amount_to_avg_ratio > 5 : reasons.append("Transaction amount is significantly above historical average.")

        if row.is_cross_border : reasons.append("Cross-border transaction.")

        if row.rapid_tx_flag : reasons.append("Rapid consecutive transaction.")

        return {

            "risk": risk,
            "probability": probability,
            "reasons": reasons
        }
        