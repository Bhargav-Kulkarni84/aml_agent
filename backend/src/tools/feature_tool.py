from src.features.transaction_features import (generate_transaction_features)
from src.features.behavioral_features import (TransactionProcessor)

class FeatureTool:

    def __init__(self):
        self.processor = TransactionProcessor()

    def run(self, df):

        #Generate transaction and behavioural features.
        df = generate_transaction_features(df)
        feature_df = self.processor.process(df)

        return feature_df