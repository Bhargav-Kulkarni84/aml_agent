import { Button } from "@/components/ui/button";
import { Input } from "@/components/ui/input";
import { Sparkles } from "lucide-react";

const suggestions = [
  "Find structuring patterns",
  "High-risk customers",
  "Layering detection",
  "Cross-border transfers",
];

export default function AIQueryBox() {
  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-8">
      <div className="flex items-center gap-3 mb-6">
        <Sparkles className="text-emerald-400" />
        <h2 className="text-2xl font-bold text-white">
          AI Investigation Agent
        </h2>
      </div>

      <p className="text-slate-400 mb-6">
        Ask Sentinel AI to analyse transactions, detect AML patterns, or
        investigate a customer.
      </p>

      <div className="flex gap-4">
        <Input
          placeholder="Find structuring patterns in last 30 days..."
          className="h-12"
        />

        <Button className="h-12 px-8">Analyse</Button>
      </div>

      <div className="flex flex-wrap gap-3 mt-6">
        {suggestions.map((item) => (
          <Button key={item} variant="outline" className="rounded-full">
            {item}
          </Button>
        ))}
      </div>
    </div>
  );
}
