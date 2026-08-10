from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.schemas.document import DocumentResponse
from app.services.document_service import DocumentService

router = APIRouter()

document_service = DocumentService()


@router.post(
    "/upload",
    response_model=DocumentResponse
)
async def upload_document(
    file: UploadFile = File(...)
):

    result = document_service.process_document(
        file
    )

    return DocumentResponse(**result)