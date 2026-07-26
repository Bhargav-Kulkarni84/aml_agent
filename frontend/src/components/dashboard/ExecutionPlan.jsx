import { CheckCircle2 } from "lucide-react";

export default function ExecutionPlan({ steps }) {
  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="mb-6 text-xl font-semibold text-white">
        🤖 AI Execution Plan
      </h2>

      <div className="space-y-4">
        {steps.map((step, index) => (
          <div key={index} className="flex gap-4">
            <CheckCircle2
              size={20}
              className="mt-1 text-green-400 flex-shrink-0"
            />

            <div>
              <h3 className="font-semibold text-white">{step.tool}</h3>

              <p className="text-sm text-slate-400">{step.reason}</p>
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}
