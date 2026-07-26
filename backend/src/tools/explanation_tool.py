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

            if row.rapid_tx_flag:
                reasons.append(
                    "Rapid consecutive transaction."
                )

            if row.amount_to_avg_ratio > 5:
                reasons.append(
                    f"Amount is {row.amount_to_avg_ratio:.1f}x the historical average."
                )

            if row.sender_fan_out_ratio > 0.8:
                reasons.append(
                    "High fan-out behavior detected."
                )

            if row.receiver_fan_in_ratio > 0.8:
                reasons.append(
                    "High fan-in behavior detected."
                )    

            reports.append({

                "risk": r,
                "probability": float(p),
                "amount": row.amount,
                "sender_account": row.sender_account,
                "receiver_account": row.receiver_account,
                "cross_border": row.is_cross_border,
                "currency_changed": row.currency_changed,
                "rapid_transaction": row.rapid_tx_flag,
                "amount_ratio": row.amount_to_avg_ratio,
                "reasons": reasons
            })

        context["reports"] = reports
        return context