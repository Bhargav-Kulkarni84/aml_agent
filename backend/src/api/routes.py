from pathlib import Path

from fastapi import APIRouter

from src.api.schemas import QueryRequest
from src.agent.aml_agent import AMLAgent

from src.preprocessing.loader import load_data
from src.preprocessing.cleaner import clean_data
from src.preprocessing.timestamp import process_timestamps

router = APIRouter()


# Load data
DATA_PATH = Path("data/raw/SAML-D.csv")

df = load_data(DATA_PATH, nrows=50000)
df = clean_data(df)
df = process_timestamps(df)

#Load agent.
agent = AMLAgent()


# get : /health
@router.get("/health")
def health() : return {"status": "ok"}


# get : /dashboard
@router.get("/dashboard")
def dashboard():

    return {
        "total_transactions": len(df),
        "laundering_transactions":int(df["is_laundering"].sum()),
        "normal_transactions":int((df["is_laundering"] == 0).sum()),
        "cross_border_transactions":int((df["sender_country"]!=df["receiver_country"]).sum()),
        "cash_transactions":int(df["payment_type"].str.contains("Cash").sum())
    }


# get : /transactions
@router.get("/transactions")
def transactions(limit: int = 100):
    return df.head(limit).to_dict(orient="records")

# get : /customers
@router.get("/customers")
def customers(limit: int = 100):

    customer_df = (
        df.groupby("sender_account").
        agg(transactions=("amount", "count"),total_sent=("amount", "sum"))
        .reset_index()
        .sort_values(
            "transactions",
            ascending=False
        )
    )

    return customer_df.head(limit).to_dict(orient="records")

# get : /analytics
@router.get("/analytics")
def analytics():

    return {
        "cross_border":int((df["sender_country"]!=df["receiver_country"]).sum()),
        "currency_conversion":int((df["payment_currency"]!=df["received_currency"]).sum()),
        "cash_withdrawals":int((df["payment_type"]=="Cash Withdrawal").sum()),
        "cash_deposits":int((df["payment_type"]=="Cash Deposit").sum())
    }


# post : /investigate
@router.post("/investigate")
def investigate(request: QueryRequest):

    result = agent.handle_query(request.query,df)
    
    return {

        "intent":result["plan"].intent,

        "confidence":result["plan"].confidence,

        "execution_plan":[
            {"tool":step.tool.value,"reason":step.reason}
            for step in result["plan"].steps
        ],

        "eda":result.get("eda"),

        "reports":result.get("reports", [])

    }