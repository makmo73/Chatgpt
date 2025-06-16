"""Placeholder CRUD operations."""

from typing import Optional
from . import models

# In-memory storage for example purposes
DOCUMENTS = []
PAGES = []

def create_document(title: str, language: Optional[str], user_id: str):
    doc_id = len(DOCUMENTS) + 1
    doc = {"id": doc_id, "title": title, "language": language, "user_id": user_id}
    DOCUMENTS.append(doc)
    return doc

def create_page(doc_id: int, page_number: int, path: str):
    page_id = len(PAGES) + 1
    page = {"id": page_id, "document_id": doc_id, "page_number": page_number, "path": path, "ocr_status": "pending"}
    PAGES.append(page)
    return page

def export_document_csv(doc_id: int):
    import io, csv
    output = io.StringIO()
    writer = csv.writer(output)
    writer.writerow(["page_number", "text"])
    for p in PAGES:
        if p["document_id"] == doc_id:
            writer.writerow([p["page_number"], f"text for page {p['id']}"])
    output.seek(0)
    return output

def export_document_pdf(doc_id: int):
    # placeholder PDF export
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    pdf.cell(0, 10, txt=f"Document {doc_id}")
    for p in PAGES:
        if p["document_id"] == doc_id:
            pdf.cell(0, 10, txt=f"Page {p['page_number']} text")
    import io
    output = io.BytesIO()
    pdf.output(output)
    output.seek(0)
    return output

def get_page(page_id: int):
    for p in PAGES:
        if p["id"] == page_id:
            return p
    raise ValueError(f"page {page_id} not found")


def get_document_language(doc_id: int) -> Optional[str]:
    for d in DOCUMENTS:
        if d["id"] == doc_id:
            return d.get("language")
    return None


EXTRACTED_TEXT = []


def save_extracted_text(page_id: int, text: str):
    rec = {"page_id": page_id, "content": text}
    EXTRACTED_TEXT.append(rec)
    for p in PAGES:
        if p["id"] == page_id:
            p["ocr_status"] = "done"
            break
    return rec
