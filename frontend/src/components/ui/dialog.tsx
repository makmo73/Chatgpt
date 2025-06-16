export function Dialog({ open, onOpenChange, children }) {
  if (!open) return null;
  return (
    <div className="dialog">
      <div className="dialog-content">
        {children}
        <button onClick={() => onOpenChange(false)}>Close</button>
      </div>
    </div>
  );
}

export function DialogContent({ children }) {
  return <div>{children}</div>;
}
