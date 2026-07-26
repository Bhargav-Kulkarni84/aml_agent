from pathlib import Path

from src.agent.aml_agent import AMLAgent
from src.preprocessing.loader import load_data
from src.preprocessing.cleaner import clean_data
from src.preprocessing.timestamp import process_timestamps

DATA_PATH = Path("data/raw/SAML-D.csv")

df = load_data(DATA_PATH, nrows=1000)
df = clean_data(df)
df = process_timestamps(df)

agent = AMLAgent()

query = input("Ask a question: ")

result = agent.handle_query(query, df)

if "eda" in result:

    print("\nDATASET SUMMARY")

    eda = result["eda"]

    print(f"Rows: {eda['rows']}")
    print(f"Duplicates: {eda['duplicates']}")

    print("\nMissing Values")

    for column, value in eda["missing"].items():
        print(f"{column:25} {value}")

    print("\nClass Distribution")

    for cls, count in eda["class_distribution"].items():
        print(f"{cls}: {count}")
        

if "reports" in result:

    reports = result["reports"]

    print("\n========== AML ANALYSIS REPORT ==========")

    print(f"Suspicious Transactions Found: {len(reports)}")

    for i, report in enumerate(reports[:5], start=1):

        print(f"\nTransaction {i}")

        print(f"Risk: {report['risk']}")
        print(f"Probability: {report['probability']:.2%}")

        print("Reasons:")

        for reason in report["reasons"]:
            print(f"  • {reason}")