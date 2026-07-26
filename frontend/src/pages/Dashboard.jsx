import Layout from "../components/layout/Layout";
import AIQueryBox from "../components/dashboard/AIQueryBox";
import KPICards from "../components/dashboard/KPICards";
import RiskChart from "../components/dashboard/RiskChart";
import ActivityChart from "../components/dashboard/ActivityChart";
import TransactionsTable from "../components/dashboard/TransactionsTable";
import SummaryCard from "../components/dashboard/SummaryCard";
import { useState } from "react";
import AgentWorkflow from "../components/dashboard/AgentWorkflow";
import { dashboardData } from "../data/dashboardData";

export default function Dashboard() {
  const [status, setStatus] = useState("idle"); // idle | loading | completed
  const [currentStep, setCurrentStep] = useState(-1);

  const handleInvestigation = () => {
    setStatus("loading");
    setCurrentStep(0);

    let step = 0;

    const interval = setInterval(() => {
      step++;

      if (step < 7) {
        setCurrentStep(step);
      } else {
        clearInterval(interval);

        setTimeout(() => {
          setStatus("completed");
          setCurrentStep(-1); // hide workflow
        }, 500);
      }
    }, 500);
  };
  return (
    <Layout>
      <div className="mx-auto max-w-7xl space-y-8">
        <AIQueryBox onInvestigate={handleInvestigation} />

        {status === "loading" && <AgentWorkflow status={currentStep} />}

        {status === "completed" && (
          <>
            <KPICards metrics={dashboardData.metrics} />

            <div className="grid grid-cols-1 gap-8 lg:grid-cols-2">
              <RiskChart data={dashboardData.riskDistribution} />
              <ActivityChart data={dashboardData.timeline} />
            </div>

            <TransactionsTable transactions={dashboardData.transactions} />

            <SummaryCard summary={dashboardData.summary} />
          </>
        )}
      </div>
    </Layout>
  );
}
