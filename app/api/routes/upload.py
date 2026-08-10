from fastapi import APIRouter, UploadFile, File

from app.schemas.document import DocumentResponse
from app.services.file_service import FileService
from app.services.pdf_service import PDFService

router = APIRouter()


@router.post(
    "/upload",
    response_model=DocumentResponse
)
async def upload_document(
    file: UploadFile = File(...)
):

    file_path = FileService.save_file(file)

    pdf = PDFService.extract_text(file_path)

    return DocumentResponse(
        filename=file.filename,
        pages=pdf["pages"],
        text=pdf["text"]
    )