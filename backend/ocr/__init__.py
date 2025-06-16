import os
from pathlib import Path
from . import engines
from .. import crud

STORAGE_PATH = os.environ.get("STORAGE_PATH", "/data")


def run_ocr_job(page_id: int, engine: str = "auto") -> str:
    """Run OCR job for the given page and return extracted text."""
    page = crud.get_page(page_id)
    lang = crud.get_document_language(page["document_id"])
    if engine == "auto":
        engine = engines.choose_engine(lang, handwriting=True)
    image_path = Path(page["path"])
    if engine == "tesseract":
        text = engines.run_tesseract(image_path, lang or "eng")
    elif engine == "google":
        text = engines.run_google_vision(image_path)
    else:
        raise ValueError(f"Unknown engine {engine}")
    crud.save_extracted_text(page_id, text)
    return text


from ..scheduler import enqueue_page
