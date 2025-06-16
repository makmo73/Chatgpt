from fastapi import FastAPI, UploadFile, File, Header, HTTPException
from fastapi.responses import StreamingResponse
from pydantic import BaseModel
from typing import List, Optional
import uuid
import shutil
from . import crud
from .ocr import STORAGE_PATH, enqueue_page

app = FastAPI(title="Handwritten OCR Service")


class DocumentIn(BaseModel):
    title: str
    language: Optional[str] = None


class PageOut(BaseModel):
    id: int
    page_number: int
    ocr_status: str


@app.post("/documents/")
async def create_document(doc: DocumentIn, x_user_id: str = Header(...)):
    return crud.create_document(title=doc.title, language=doc.language, user_id=x_user_id)


@app.post("/documents/{doc_id}/pages/", response_model=List[PageOut])
async def upload_pages(doc_id: int, files: List[UploadFile] = File(...)):
    pages = []
    for num, f in enumerate(files, 1):
        dest = f"{STORAGE_PATH}/{uuid.uuid4()}.png"
        with open(dest, "wb") as out:
            shutil.copyfileobj(f.file, out)
        page = crud.create_page(doc_id, num, dest)
        enqueue_page(page["id"])
        pages.append(page)
    return pages


@app.get("/documents/{doc_id}/export/csv")
async def export_csv(doc_id: int):
    data = crud.export_document_csv(doc_id)
    return StreamingResponse(data, media_type="text/csv")


@app.get("/documents/{doc_id}/export/pdf")
async def export_pdf(doc_id: int):
    data = crud.export_document_pdf(doc_id)
    return StreamingResponse(data, media_type="application/pdf")
