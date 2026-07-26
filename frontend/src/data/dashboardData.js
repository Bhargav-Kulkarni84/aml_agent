export const dashboardData = {
  metrics: {
    totalTransactions: 15234,
    suspiciousTransactions: 28,
    highRiskCustomers: 7,
    riskScore: 82,
  },

  riskDistribution: [
    { name: "High", value: 7 },
    { name: "Medium", value: 18 },
    { name: "Low", value: 103 },
  ],

  timeline: [
    { day: "Mon", suspicious: 4 },
    { day: "Tue", suspicious: 6 },
    { day: "Wed", suspicious: 3 },
    { day: "Thu", suspicious: 9 },
    { day: "Fri", suspicious: 5 },
  ],

  transactions: [
    {
      id: "TXN-1045",
      customer: "John Doe",
      amount: "$18,500",
      country: "Singapore",
      risk: "High",
      reason: "Structuring",
    },
    {
      id: "TXN-1046",
      customer: "Alice Smith",
      amount: "$7,400",
      country: "India",
      risk: "Medium",
      reason: "Rapid Transfers",
    },
    {
      id: "TXN-1047",
      customer: "David Lee",
      amount: "$22,000",
      country: "UAE",
      risk: "High",
      reason: "Layering",
    },
  ],

  summary: {
    confidence: 94,
    recommendation: "Generate SAR",
    explanation:
      "Multiple transactions were detected below the reporting threshold across several accounts, indicating possible structuring activity.",
  },
};