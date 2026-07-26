export default function TransactionsTable({ transactions }) {
  return (
    <div className="rounded-2xl border border-slate-800 bg-slate-900 p-6">
      <h2 className="mb-5 text-lg font-semibold text-white">
        Flagged Transactions
      </h2>

      <div className="overflow-x-auto">
        <table className="w-full text-left">
          <thead className="text-slate-400">
            <tr>
              <th className="pb-4">ID</th>
              <th>Customer</th>
              <th>Amount</th>
              <th>Country</th>
              <th>Risk</th>
              <th>Reason</th>
            </tr>
          </thead>

          <tbody>
            {transactions.map((tx) => (
              <tr key={tx.id} className="border-t border-slate-800">
                <td className="py-4">{tx.id}</td>
                <td>{tx.customer}</td>
                <td>{tx.amount}</td>
                <td>{tx.country}</td>

                <td>
                  <span className="rounded-full bg-red-500/20 px-3 py-1 text-red-400">
                    {tx.risk}
                  </span>
                </td>

                <td>{tx.reason}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
