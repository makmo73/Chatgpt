import os
from celery import Celery
from .ocr import run_ocr_job

CELERY_BROKER = os.environ.get("REDIS_URL", "redis://redis:6379/0")
CELERY_BACKEND = os.environ.get("REDIS_URL", "redis://redis:6379/1")

celery_app = Celery("tasks", broker=CELERY_BROKER, backend=CELERY_BACKEND)

BATCH_THRESHOLD = int(os.environ.get("BATCH_THRESHOLD", "50"))

@celery_app.task
def process_page(page_id: int, engine: str):
    run_ocr_job(page_id, engine)


def enqueue_page(page_id: int, engine: str = "auto") -> None:
    process_page.delay(page_id, engine)
