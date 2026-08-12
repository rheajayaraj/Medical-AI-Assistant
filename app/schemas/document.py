from pydantic import BaseModel
from typing import Optional


class DocumentResponse(BaseModel):
    document_id: Optional[str] = None
    filename: str
    pages: int
    total_chunks: int
    status: str