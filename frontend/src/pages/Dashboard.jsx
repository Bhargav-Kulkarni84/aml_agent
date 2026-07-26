import Layout from "../components/layout/Layout";
import AIQueryBox from "../components/dashboard/AIQueryBox";
import KPICards from "../components/dashboard/KPICards";
import RiskChart from "../components/dashboard/RiskChart";
import ActivityChart from "../components/dashboard/ActivityChart";
import TransactionsTable from "../components/dashboard/TransactionsTable";
import SummaryCard from "../components/dashboard/SummaryCard";

import { dashboardData } from "../data/dashboardData";

export default function Dashboard() {
  return (
    <Layout>
      <div className="mx-auto max-w-7xl space-y-8">
        <AIQueryBox />

        <KPICards metrics={dashboardData.metrics} />

        <div className="grid grid-cols-1 gap-8 lg:grid-cols-2">
          <RiskChart data={dashboardData.riskDistribution} />

          <ActivityChart data={dashboardData.timeline} />
        </div>

        <TransactionsTable transactions={dashboardData.transactions} />

        <SummaryCard summary={dashboardData.summary} />
      </div>
    </Layout>
  );
}
