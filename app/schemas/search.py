from pydantic import BaseModel


class SearchRequest(BaseModel):
    query: str


class SearchResult(BaseModel):
    document: str
    metadata: dict
    score: float


class SearchResponse(BaseModel):
    query: str
    results: list[SearchResult]