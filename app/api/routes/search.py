from fastapi import APIRouter

from app.schemas.search import (
    SearchRequest,
    SearchResponse,
    SearchResult
)

from app.services.search_service import SearchService

router = APIRouter()

search_service = SearchService()


@router.post(
    "/search",
    response_model=SearchResponse
)
def semantic_search(
    request: SearchRequest
):

    return search_service.search(
        request.query,
    )