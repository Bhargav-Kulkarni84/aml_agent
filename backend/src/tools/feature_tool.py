from src.features.transaction_features import (generate_transaction_features)
from src.features.behavioral_features import (TransactionProcessor)

class FeatureTool:

    def __init__(self):
        self.processor = TransactionProcessor()

    def run(self, context):

        df = context["data"]

        df = generate_transaction_features(df)
        feature_df = self.processor.process(df)

        context["feature_df"] = feature_df

        return context