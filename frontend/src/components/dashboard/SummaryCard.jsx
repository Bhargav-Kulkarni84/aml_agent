import { Bot } from "lucide-react";

export default function SummaryCard({ summary }) {
  return (
    <div className="rounded-2xl border border-emerald-500/30 bg-slate-900 p-6">
      <div className="flex items-center gap-3">
        <Bot className="text-emerald-400" />

        <h2 className="text-xl font-semibold text-white">
          AI Investigation Summary
        </h2>
      </div>

      <p className="mt-6 text-slate-300">{summary.explanation}</p>

      <div className="mt-6 flex gap-6">
        <div>
          <p className="text-slate-400 text-sm">Confidence</p>

          <h3 className="text-white font-bold">{summary.confidence}%</h3>
        </div>

        <div>
          <p className="text-slate-400 text-sm">Recommendation</p>

          <h3 className="font-bold text-emerald-400">
            {summary.recommendation}
          </h3>
        </div>
      </div>
    </div>
  );
}
