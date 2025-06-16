from pydantic import BaseModel
from typing import Optional

class Document(BaseModel):
    id: int
    title: str
    language: Optional[str] = None
    user_id: str

class Page(BaseModel):
    id: int
    document_id: int
    page_number: int
    path: str
    ocr_status: str
