import joblib

class AnomalyTool:

    def __init__(self):

        self.model = joblib.load("models/aml_model.pkl")
        self.columns = joblib.load("models/feature_columns.pkl")

        def run(self, feature_df):

            drop_columns = [
                "sender_account",
                "receiver_account",
                "timestamp",
                "laundering_type",
                "is_laundering"
            ]

            X = feature_df.drop(columns=drop_columns)
            X = X[self.columns]
            prob = self.model.predict_proba(X)[:,1]
            prediction = prob > 0.5

            return {
                "probability": prob,
                "prediction": prediction
            }