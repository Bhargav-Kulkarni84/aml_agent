import { Bot, Brain, Target } from "lucide-react";

export default function SummaryCard({ report, confidence, intent }) {
  const formatReport = (text) => {
    if (!text) return [];

    return text.split("\n").map((line, index) => {
      line = line.trim();

      if (line.startsWith("# ")) {
        return (
          <h2
            key={index}
            className="mt-8 mb-3 text-2xl font-bold text-white border-b border-slate-700 pb-2"
          >
            {line.replace("# ", "")}
          </h2>
        );
      }

      if (line.startsWith("- ")) {
        return (
          <li key={index} className="ml-6 list-disc text-slate-300 mb-2">
            {line.replace("- ", "")}
          </li>
        );
      }

      if (line.startsWith("* ")) {
        return (
          <li key={index} className="ml-6 list-disc text-slate-300 mb-2">
            {line.replace("* ", "")}
          </li>
        );
      }

      if (line === "") return <br key={index} />;

      return (
        <p key={index} className="text-slate-300 leading-8">
          {line}
        </p>
      );
    });
  };

  return (
    <div className="rounded-2xl border border-emerald-500/30 bg-slate-900 p-8">
      <div className="flex items-center gap-3 mb-8">
        <Bot className="text-emerald-400" />

        <h1 className="text-2xl font-bold text-white">
          AI Investigation Report
        </h1>
      </div>

      <div className="grid md:grid-cols-2 lg:grid-cols-3 gap-6 mb-8">
        <div className="rounded-xl bg-slate-800 p-4">
          <div className="flex items-center gap-2 mb-2">
            <Target size={18} className="text-cyan-400" />
            <p className="text-slate-400 text-sm">Intent</p>
          </div>

          <h3 className="font-semibold text-white">
            {intent.replaceAll("_", " ")}
          </h3>
        </div>

        <div className="rounded-xl bg-slate-800 p-4">
          <div className="flex items-center gap-2 mb-2">
            <Brain size={18} className="text-emerald-400" />
            <p className="text-slate-400 text-sm">AI Confidence</p>
          </div>

          <h3 className="font-semibold text-emerald-400">{confidence}%</h3>
        </div>
      </div>

      <div className="max-h-[650px] overflow-y-auto rounded-xl">
        {formatReport(report)}
      </div>
    </div>
  );
}
