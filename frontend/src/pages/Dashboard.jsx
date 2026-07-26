import { useState } from "react";

import Layout from "../components/layout/Layout";
import AIQueryBox from "../components/dashboard/AIQueryBox";
import AgentWorkflow from "../components/dashboard/AgentWorkflow";
import KPICards from "../components/dashboard/KPICards";
import RiskChart from "../components/dashboard/RiskChart";
import TransactionsTable from "../components/dashboard/TransactionsTable";
import SummaryCard from "../components/dashboard/SummaryCard";
import ExecutionPlan from "../components/dashboard/ExecutionPlan";

import { investigate } from "../services/dashboardService";

export default function Dashboard() {
  const [status, setStatus] = useState("idle");

  const [currentStep, setCurrentStep] = useState(-1);

  const [result, setResult] = useState(null);

  const handleInvestigation = async (query) => {
    setStatus("loading");
    setCurrentStep(0);

    let step = 0;

    const interval = setInterval(() => {
      step++;

      if (step < 5) {
        setCurrentStep(step);
      }
    }, 800);

    try {
      const response = await investigate(query);

      clearInterval(interval);

      setResult(response);

      setStatus("completed");
    } catch (err) {
      clearInterval(interval);
      console.error(err);
      setStatus("idle");
    }
  };

  return (
    <Layout>
      <div className="mx-auto max-w-7xl space-y-8">
        <AIQueryBox onInvestigate={handleInvestigation} />

        {status === "loading" && <AgentWorkflow status={currentStep} />}

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
