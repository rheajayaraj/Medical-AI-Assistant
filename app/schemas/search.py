from pydantic import BaseModel


class SearchRequest(BaseModel):
    query: str
    top_k: int = 3


class SearchResult(BaseModel):
    document: str
    metadata: dict


class SearchResponse(BaseModel):
    query: str
    results: list[SearchResult]