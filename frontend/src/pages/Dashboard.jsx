import Layout from "../components/layout/Layout";
import AIQueryBox from "../components/dashboard/AIQueryBox";

export default function Dashboard() {
  return (
    <Layout>
      <div className="max-w-5xl mx-auto">
        <AIQueryBox />

        <div className="mt-10 rounded-2xl border border-dashed border-slate-700 p-16 text-center">
          <h2 className="text-xl font-semibold text-slate-300">
            Ready to Investigate
          </h2>

          <p className="mt-3 text-slate-500">
            Enter a natural language query above to start an AML investigation.
            The AI agent will analyze transactions, detect anomalies, and
            generate explainable insights.
          </p>
        </div>
      </div>
    </Layout>
  );
}
