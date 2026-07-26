import { Activity, AlertTriangle, ShieldAlert, TrendingUp } from "lucide-react";

const iconMap = {
  totalTransactions: Activity,
  suspiciousTransactions: AlertTriangle,
  highRiskCustomers: ShieldAlert,
  riskScore: TrendingUp,
};

export default function KPICards({ metrics }) {
  const cards = [
    {
      key: "totalTransactions",
      title: "Total Transactions",
      value: metrics.totalTransactions.toLocaleString(),
    },
    {
      key: "suspiciousTransactions",
      title: "Suspicious",
      value: metrics.suspiciousTransactions,
    },
    {
      key: "highRiskCustomers",
      title: "High Risk",
      value: metrics.highRiskCustomers,
    },
    {
      key: "riskScore",
      title: "Risk Score",
      value: `${metrics.riskScore}%`,
    },
  ];

  return (
    <div className="grid grid-cols-1 gap-5 md:grid-cols-2 xl:grid-cols-4">
      {cards.map((card) => {
        const Icon = iconMap[card.key];

        return (
          <div
            key={card.title}
            className="rounded-2xl border border-slate-800 bg-slate-900 p-6"
          >
            <div className="flex items-center justify-between">
              <span className="text-sm text-slate-400">{card.title}</span>

              <Icon size={20} className="text-emerald-400" />
            </div>

            <h2 className="mt-5 text-3xl font-bold text-white">{card.value}</h2>
          </div>
        );
      })}
    </div>
  );
}
