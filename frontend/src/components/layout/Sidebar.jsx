import {
  LayoutDashboard,
  ShieldAlert,
  Users,
  BarChart3,
  FileText,
} from "lucide-react";

const menuItems = [
  {
    title: "Dashboard",
    icon: LayoutDashboard,
  },
  {
    title: "Transactions",
    icon: ShieldAlert,
  },
  {
    title: "Customers",
    icon: Users,
  },
  {
    title: "Analytics",
    icon: BarChart3,
  },
  {
    title: "Reports",
    icon: FileText,
  },
];

export default function Sidebar() {
  return (
    <aside className="w-64 bg-slate-900 border-r border-slate-800 min-h-screen flex flex-col">
      <div className="p-6">
        <h1 className="text-2xl font-bold text-white">FinSentinel AI</h1>

        <p className="text-sm text-slate-400 mt-1">
          AML Investigation Platform
        </p>
      </div>

      <nav className="flex-1 px-4 space-y-2">
        {menuItems.map((item) => {
          const Icon = item.icon;

          return (
            <button
              key={item.title}
              className="w-full flex items-center gap-3 rounded-xl px-4 py-3 text-slate-300 hover:bg-slate-800 hover:text-white transition"
            >
              <Icon size={20} />
              {item.title}
            </button>
          );
        })}
      </nav>
    </aside>
  );
}
