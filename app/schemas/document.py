from pydantic import BaseModel


class DocumentResponse(BaseModel):
    document_id: str
    filename: str
    pages: int
    total_chunks: int
    status: str