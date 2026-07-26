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
              <th>Sender</th>
              <th>Receiver</th>
              <th>Amount</th>
              <th>Risk</th>
              <th>Cross Border</th>
              <th>Currency</th>
              <th>Probability</th>
            </tr>
          </thead>

          <tbody>
            {transactions.map((tx) => (
              <tr
                key={tx.id}
                className="border-t border-slate-800 text-slate-200"
              >
                <td className="py-4">{tx.id}</td>

                <td>{tx.sender}</td>

                <td>{tx.receiver}</td>

                <td className="text-white font-medium">
                  ${tx.amount.toLocaleString()}
                </td>

                <td>
                  <span
                    className={`rounded-full px-3 py-1 text-sm ${
                      tx.risk === "High"
                        ? "bg-red-500/20 text-red-400"
                        : tx.risk === "Medium"
                          ? "bg-yellow-500/20 text-yellow-400"
                          : "bg-green-500/20 text-green-400"
                    }`}
                  >
                    {tx.risk}
                  </span>
                </td>

                <td>{tx.crossBorder}</td>

                <td>{tx.currencyChanged}</td>

                <td>{tx.probability}</td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );
}
