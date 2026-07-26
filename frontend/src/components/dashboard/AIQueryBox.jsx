import { useState } from "react";
import { Sparkles } from "lucide-react";
import SuggestedQueries from "./SuggestedQueries";

export default function AIQueryBox({ onInvestigate }) {
  const [query, setQuery] = useState("");

  const handleInvestigate = () => {
    if (!query.trim()) return;

    onInvestigate(query);
  };

  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-8 shadow-lg">
      <span className="inline-flex items-center gap-2 rounded-full bg-emerald-500/10 px-4 py-1 text-sm text-emerald-400 border border-emerald-500/30">
        <Sparkles size={16} />
        AI Powered Investigation
      </span>

      <h1 className="mt-8 text-3xl font-bold text-white">Ask FinSentinel AI</h1>

      <p className="mt-2 text-slate-400">
        Investigate suspicious transactions using natural language. The AI agent
        will determine the required AML checks automatically.
      </p>

      <div className="mt-8 flex gap-4">
        <input
          value={query}
          onChange={(e) => setQuery(e.target.value)}
          placeholder="e.g. Find structuring patterns in the last 30 days..."
          className="flex-1 rounded-xl border border-slate-700 bg-slate-950 px-5 py-4 text-white outline-none transition focus:border-emerald-500"
        />

        <button
          onClick={handleInvestigate}
          className="rounded-xl bg-emerald-500 px-8 py-4 font-semibold text-black transition hover:bg-emerald-400"
        >
          Investigate
        </button>
      </div>

      <SuggestedQueries onSelect={setQuery} />
    </div>
  );
}
