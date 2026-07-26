import { CheckCircle2, Loader2, Circle } from "lucide-react";

export default function AgentWorkflow({ status }) {
  const steps = [
    "Loading transaction dataset",
    "Running EDA",
    "Engineering features",
    "Building customer profile",
    "Running anomaly detection",
    "Risk assessment",
    "Generating AI explanation",
  ];

  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="mb-6 text-xl font-semibold text-white">
        🤖 AI Investigation Workflow
      </h2>

      <div className="space-y-4">
        {steps.map((step, index) => (
          <div key={step} className="flex items-center gap-3">
            {index < status ? (
              <CheckCircle2 className="text-green-400" size={20} />
            ) : index === status ? (
              <Loader2 className="animate-spin text-yellow-400" size={20} />
            ) : (
              <Circle className="text-slate-500" size={18} />
            )}

            <span className="text-slate-300">{step}</span>
          </div>
        ))}
      </div>
    </div>
  );
}
