from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService
from app.core.config import settings


class SearchService:

    def __init__(self):

        self.vector_service = VectorService()

    def search(
        self,
        query,
    ):

        embedding = EmbeddingService.generate_embedding(
            query
        )

        response= self.vector_service.search(
            embedding,
            top_k=settings.SEARCH_TOP_K
        )

        results = []

        if response["documents"]:

            for document, metadata, distance in zip(
                response["documents"][0],
                response["metadatas"][0],
                response["distances"][0]
            ):

                similarity = 1 / (1 + distance)
                if similarity < 0.45:
                    continue

                results.append({
                    "document": document,
                    "metadata": metadata,
                    "score": similarity
                })

        results.sort(key=lambda x: x["score"], reverse=True)
        results = results[:3]

        return {
            "query": query,
            "results": results
        }