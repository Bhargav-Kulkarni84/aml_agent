import joblib

class AnomalyTool:

    def __init__(self):

        self.model = joblib.load("src/models/aml_model.pkl")
        self.columns = joblib.load("src/models/feature_columns.pkl")

    def run(self, context):

        feature_df = context["feature_df"]

        drop_columns = [
            "sender_account",
            "receiver_account",
            "timestamp",
            "laundering_type",
            "is_laundering"
        ]

        X = feature_df.drop(columns=drop_columns)
        X = X[self.columns]

        probability = self.model.predict_proba(X)[:,1]
        prediction = probability > 0.35

        context["probability"] = probability
        context["prediction"] = prediction
        
        return context