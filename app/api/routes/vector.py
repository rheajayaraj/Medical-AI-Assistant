from fastapi import APIRouter

from app.services.vector_service import VectorService

router = APIRouter()

vector_service = VectorService()


@router.get("/vector-count")
def vector_count():

   return {
    "documents": vector_service.collection.count()
    }