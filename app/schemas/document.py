from pydantic import BaseModel


class DocumentResponse(BaseModel):
    filename: str
    pages: int
    text: str