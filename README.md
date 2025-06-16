# OCR/HTR Document Digitization

This repository contains a minimal skeleton to run an OCR/HTR service using FastAPI, Celery and React.

## Quickstart

1. Copy `.env.example` to `.env` and adjust variables if needed.
2. Build and start the stack with Docker Compose:
   ```bash
   docker-compose up --build
   ```
3. Access the frontend at <http://localhost:3000>.

The backend exposes endpoints for creating documents, uploading pages and exporting CSV/PDF. OCR jobs are processed asynchronously using Celery. The `ocr` module chooses between Tesseract and Google Vision depending on language and handwriting.

The `.env` file also allows configuring credentials for Google Vision via `GOOGLE_APPLICATION_CREDENTIALS`.
