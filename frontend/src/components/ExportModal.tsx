import { Dialog, DialogContent } from "@/components/ui/dialog";
import { Button } from "@/components/ui/button";

export function ExportModal({ open, onClose, onExportCSV, onExportPDF }) {
  return (
    <Dialog open={open} onOpenChange={onClose}>
      <DialogContent>
        <Button onClick={onExportCSV}>Export CSV</Button>
        <Button onClick={onExportPDF}>Export PDF</Button>
      </DialogContent>
    </Dialog>
  );
}
