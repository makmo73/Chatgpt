export function DataTable({ columns, data }) {
  return (
    <table>
      <thead>
        <tr>{columns.map(c => <th key={c}>{c}</th>)}</tr>
      </thead>
      <tbody>
        {data?.map((row, i) => (
          <tr key={i}>{columns.map(c => <td key={c}>{row[c]}</td>)}</tr>
        ))}
      </tbody>
    </table>
  );
}
