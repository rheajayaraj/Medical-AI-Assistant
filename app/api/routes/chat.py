from fastapi import APIRouter

from app.schemas.chat import ChatRequest, ChatResponse
from app.services.rag_service import RAGService

router = APIRouter()

rag = RAGService()


@router.post(
    "/chat",
    response_model=ChatResponse
)
def chat(request: ChatRequest):

    return rag.ask(
    query=request.question,
    session_id=request.session_id
)