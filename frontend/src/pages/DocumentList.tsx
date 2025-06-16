import { useQuery } from "@tanstack/react-query";
import { Link } from "react-router-dom";
import { Button } from "@/components/ui/button";
import { DataTable } from "@/components/ui/data-table";

export default function DocumentList() {
  const { data, isLoading } = useQuery(["documents"], fetchDocuments);

  if (isLoading) return <div>Loading...</div>;

  return (
    <div className="p-4">
      <h1 className="text-xl font-bold mb-4">Documenti</h1>
      <Link to="/upload">
        <Button>Carica nuovo</Button>
      </Link>
      <DataTable columns={columns} data={data} />
    </div>
  );
}
