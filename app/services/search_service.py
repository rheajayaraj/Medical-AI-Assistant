from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService


class SearchService:

    def __init__(self):

        self.vector_service = VectorService()

    def search(
        self,
        query,
        top_k=3
    ):

        embedding = EmbeddingService.generate_embedding(
            query
        )

        return self.vector_service.search(
            embedding,
            top_k
        )