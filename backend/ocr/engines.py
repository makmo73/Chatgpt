import subprocess
from pathlib import Path
from typing import Optional

try:
    from google.cloud import vision
except ImportError:  # pragma: no cover - google cloud optional
    vision = None


def run_tesseract(image_path: Path, lang: str = "eng") -> str:
    """Run tesseract on the given image and return extracted text."""
    result = subprocess.run([
        "tesseract", str(image_path), "stdout", "-l", lang
    ], capture_output=True, text=True, check=False)
    return result.stdout


def run_google_vision(image_path: Path) -> str:
    """Use Google Vision API to extract text."""
    if vision is None:
        raise RuntimeError("google-cloud-vision not installed")
    client = vision.ImageAnnotatorClient()
    with open(image_path, "rb") as f:
        content = f.read()
    image = vision.Image(content=content)
    response = client.text_detection(image=image)
    if response.error.message:
        raise RuntimeError(response.error.message)
    return response.full_text_annotation.text


def choose_engine(language: Optional[str], handwriting: bool = False) -> str:
    """Simple engine selection based on language and handwriting flag."""
    if handwriting:
        # cloud engine recommended for handwriting
        return "google"
    if language and language.lower() not in {"en", "it"}:
        # languages other than en/it use Google
        return "google"
    return "tesseract"
