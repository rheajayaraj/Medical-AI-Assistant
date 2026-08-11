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

    response = search_service.search(
        request.query,
        request.top_k
    )

    documents = response["documents"][0]

    metadata = response["metadatas"][0]

    results = []

    for doc, meta in zip(
        documents,
        metadata
    ):

        results.append(

            SearchResult(

                document=doc,

                metadata=meta

            )

        )

    return SearchResponse(

        query=request.query,

        results=results

    )