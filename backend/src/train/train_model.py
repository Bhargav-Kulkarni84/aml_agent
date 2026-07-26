from pathlib import Path

# Import preprocessing functions
from src.preprocessing.loader import load_data
from src.preprocessing.cleaner import clean_data
from src.preprocessing.timestamp import process_timestamps
from src.features.transaction_features import generate_transaction_features

# Import behavioral feature generator
from src.features.behavioral_features import TransactionProcessor

# Function to split dataset into train/test sets
from sklearn.model_selection import train_test_split

# XGBoost classifier
from xgboost import XGBClassifier

# Model evaluation metrics
from sklearn.metrics import (
    classification_report,
    confusion_matrix,
    roc_auc_score,
)

# Save and load trained models
import joblib

# Path to the dataset
DATA_PATH = Path("data/raw/SAML-D.csv")

# Load only the first 2 million rows during development
DEV_ROWS = 2_000_000

# STEP 1 Load and preprocess data
df = load_data(DATA_PATH, nrows=DEV_ROWS)
df = clean_data(df)
df = process_timestamps(df)
df = generate_transaction_features(df)

# STEP 2: Generate behavioral features
processor = TransactionProcessor()
feature_df = processor.process(df)

# STEP 3: Separate labels and features
# Target variable (0 = normal, 1 = laundering)
y = feature_df["is_laundering"]

# Remove columns that should not be used for training
X = feature_df.drop(
    columns=[
        "is_laundering",      # Target column
        "sender_account",     # Identifier
        "receiver_account",   # Identifier
        "timestamp",          # Raw datetime
        "laundering_type",    # Future information (label leakage)
    ]
)


# STEP 4: Split into train/test
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,     # 80% training, 20% testing
    random_state=42,   # Reproducible split
    stratify=y,        # Preserve class proportions
)

# STEP 5: Create the model
model = XGBClassifier(
    n_estimators=200,          # Number of trees
    max_depth=6,               # Maximum tree depth
    learning_rate=0.1,         # Learning speed
    objective="binary:logistic",  # Binary classification
    eval_metric="logloss",     # Evaluation metric
    random_state=42,
)

# STEP 6: Train the model
model.fit(X_train, y_train)

# STEP 7: Make predictions
pred = model.predict(X_test)

# STEP 8: Evaluate the model
print(classification_report(y_test, pred))
print(confusion_matrix(y_test, pred))
print(roc_auc_score(y_test,model.predict_proba(X_test)[:, 1]))

# STEP 9: Save the trained model
joblib.dump(model, "aml_model.pkl")