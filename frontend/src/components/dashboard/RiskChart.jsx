import {
  PieChart,
  Pie,
  Cell,
  ResponsiveContainer,
  Tooltip,
  Legend,
} from "recharts";

const COLORS = ["#ef4444", "#f59e0b", "#10b981"];

export default function RiskChart({ data }) {
  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="mb-5 text-lg font-semibold text-white">
        Risk Distribution
      </h2>

      <ResponsiveContainer width="100%" height={320}>
        <PieChart>
          <Pie
            data={data}
            dataKey="value"
            nameKey="name"
            outerRadius={100}
            label={({ name, value }) => `${name}: ${value}`}
          >
            {data.map((entry, index) => (
              <Cell key={entry.name} fill={COLORS[index % COLORS.length]} />
            ))}
          </Pie>

          <Tooltip />

          <Legend
            wrapperStyle={{
              color: "#fff",
            }}
          />
        </PieChart>
      </ResponsiveContainer>
    </div>
  );
}
