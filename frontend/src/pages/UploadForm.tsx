import { useMutation } from "@tanstack/react-query";
import { useState } from "react";
import { Button } from "@/components/ui/button";

export default function UploadForm() {
  const [files, setFiles] = useState<FileList | null>(null);
  const mutation = useMutation(uploadFiles);

  return (
    <form onSubmit={e => { e.preventDefault(); mutation.mutate(files); }}>
      <input multiple type="file" onChange={e => setFiles(e.target.files)} />
      <Button type="submit" disabled={mutation.isLoading}>Upload</Button>
    </form>
  );
}
