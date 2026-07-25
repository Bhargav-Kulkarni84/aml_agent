const suggestions = [
  "Find structuring patterns in the last 30 days",
  "Identify high-risk customers",
  "Detect layering transactions",
  "Show suspicious cross-border transfers",
  "Generate AML investigation report",
  "Find unusual cash withdrawals",
];

export default function SuggestedQueries({ onSelect }) {
  return (
    <div className="mt-6">
      <h3 className="text-sm font-medium text-slate-400 mb-3">
        Suggested Investigations
      </h3>

      <div className="flex flex-wrap gap-3">
        {suggestions.map((item) => (
          <button
            key={item}
            onClick={() => onSelect(item)}
            className="rounded-full border border-slate-700 bg-slate-900 px-4 py-2 text-sm text-slate-300 transition hover:border-emerald-500 hover:text-white hover:bg-slate-800"
          >
            {item}
          </button>
        ))}
      </div>
    </div>
  );
}
