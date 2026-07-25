import Sidebar from "./Sidebar";
import Navbar from "./Navbar";

export default function Layout({ children }) {
  return (
    <div className="bg-slate-950 min-h-screen flex">
      <Sidebar />

      <div className="flex-1 flex flex-col">
        <Navbar />

        <main className="p-8 flex-1 overflow-auto">{children}</main>
      </div>
    </div>
  );
}
