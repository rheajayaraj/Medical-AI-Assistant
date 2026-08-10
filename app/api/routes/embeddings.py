import uuid
from fastapi import APIRouter

from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService

router = APIRouter()


@router.get("/test-embedding")
def test_embedding():

    embeddings = EmbeddingService.generate_embeddings(
       [

            {
                "chunk_id": str(uuid.uuid4()),
                "text": "Hypertension"
            },

            {
                "chunk_id": str(uuid.uuid4()),
                "text": "High blood pressure"
            },

            {
                "chunk_id": str(uuid.uuid4()),
                "text": "Chocolate cake"
            }

        ]
    )

    vector_service = VectorService()

    vector_service.add_embeddings(
        embeddings
    )

    return {

        "dimensions": len(
            embeddings[0]["embedding"]
        ),

        "total": len(embeddings)

    }