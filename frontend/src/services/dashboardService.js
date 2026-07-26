import agentAPI from "./agent";

export const investigate = async (query) => {
  const { data } = await agentAPI.post("/investigate", {
  query,
});

  const summary = data.summary;

  const metrics = {
    totalTransactions: summary.transactions_analyzed,
    suspiciousTransactions: summary.flagged_transactions,
    highRiskTransactions: summary.high_risk_transactions,
    aiConfidence: Math.round(data.confidence * 100),
  };

  const riskDistribution = [
    {
      name: "High",
      value: summary.high_risk_transactions,
    },
    {
      name: "Medium",
      value:
        summary.flagged_transactions -
        summary.high_risk_transactions,
    },
    {
      name: "Low",
      value:
        summary.transactions_analyzed -
        summary.flagged_transactions,
    },
  ];

  const transactions = (data.top_alerts || [])
  .sort((a, b) => b.probability - a.probability)
  .map((tx, index) => ({
    id: index + 1,
    sender: tx.sender_account,
    receiver: tx.receiver_account,
    amount: tx.amount,
    risk: tx.risk,
    probability: `${(tx.probability * 100).toFixed(2)}%`,
    crossBorder: tx.cross_border ? "Yes" : "No",
    currencyChanged: tx.currency_changed ? "Yes" : "No",
    reasons: tx.reasons.join(", "),
  }));

  return {
  intent: data.intent,
  confidence: metrics.aiConfidence,
  executionPlan: data.execution_plan || [],
  metrics,
  riskDistribution,
  transactions,
  report: data.report || "No investigation report generated.",
  };
};