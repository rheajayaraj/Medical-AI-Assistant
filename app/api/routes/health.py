from fastapi import APIRouter

router = APIRouter()


@router.get("/health")
def health():
    return {
        "status": "healthy"
    }


@router.get("/about")
def about():
    return {
        "project": "Medical AI Assistant",
        "author": "Rhea Jayaraj",
        "purpose": "Medical RAG Assistant"
    }