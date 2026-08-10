from fastapi import APIRouter
from fastapi import UploadFile
from fastapi import File

from app.services.file_service import FileService

router = APIRouter()


@router.post("/upload")
async def upload_document(
    file: UploadFile = File(...)
):

    file_path = FileService.save_file(file)

    return {
        "message": "Upload successful",
        "filename": file.filename,
        "saved_to": str(file_path)
    }