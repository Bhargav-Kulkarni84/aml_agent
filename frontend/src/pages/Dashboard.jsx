import { useState } from "react";

import Layout from "../components/layout/Layout";
import AIQueryBox from "../components/dashboard/AIQueryBox";
import Loader from "../components/dashboard/Loader";
import KPICards from "../components/dashboard/KPICards";
import RiskChart from "../components/dashboard/RiskChart";
import TransactionsTable from "../components/dashboard/TransactionsTable";
import SummaryCard from "../components/dashboard/SummaryCard";
import ExecutionPlan from "../components/dashboard/ExecutionPlan";

import { investigate } from "../services/dashboardService";

export default function Dashboard() {
  const [status, setStatus] = useState("idle");

  const [result, setResult] = useState(null);

  const handleInvestigation = async (query) => {
    setStatus("loading");

    try {
      const response = await investigate(query);

      setResult(response);

      setStatus("completed");
    } catch (err) {
      console.error(err);
      setStatus("idle");
    }
  };

  return (
    <Layout>
      <div className="mx-auto max-w-7xl space-y-8">
        <AIQueryBox onInvestigate={handleInvestigation} />

        {status === "loading" && <Loader />}

        {status === "completed" && result && (
          <>
            <KPICards metrics={result.metrics} />

            <RiskChart data={result.riskDistribution} />

            <TransactionsTable transactions={result.transactions} />
            <ExecutionPlan steps={result.executionPlan} />

            <SummaryCard
              report={result.report}
              confidence={result.confidence}
              intent={result.intent}
            />
          </>
        )}
      </div>
    </Layout>
  );
}
