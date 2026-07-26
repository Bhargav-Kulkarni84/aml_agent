class ExplanationTool:

    def run(self, context):

        feature_df = context["feature_df"]
        probability = context["probability"]
        risk = context["risk"]

        reports = []

        for row, p, r , pred in zip(
            feature_df.itertuples(index=False),
            probability,
            risk,
            context["prediction"]
        ):

            
            if not pred: continue

            reasons = []

            # Example explanations
            if row.is_cross_border:
                reasons.append("Cross-border transaction.")

            if row.currency_changed:
                reasons.append("Currency conversion detected.")

            if p > 0.9:
                reasons.append("High ML confidence.")

            reports.append({
                "risk": r,
                "probability": float(p),
                "reasons": reasons
            })

        context["reports"] = reports
        return context