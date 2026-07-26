import { Loader2, ShieldAlert } from "lucide-react";

export default function Loader() {
  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-12 text-center">
      <ShieldAlert className="mx-auto mb-6 text-emerald-400" size={48} />

      <Loader2
        className="mx-auto mb-6 animate-spin text-emerald-400"
        size={40}
      />

      <h2 className="text-2xl font-semibold text-white">
        Running AML Investigation...
      </h2>

      <p className="mt-3 text-slate-400">
        Analyzing transactions, assessing risk, and generating the AI
        investigation report...
      </p>
    </div>
  );
}
