from pydantic import BaseModel


class EmbeddingResponse(BaseModel):

    chunk_id: int

    dimensions: int