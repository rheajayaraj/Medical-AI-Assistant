import uuid

from app.services.file_service import FileService
from app.services.pdf_service import PDFService
from app.services.chunk_service import ChunkService
from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService


class DocumentService:

    def __init__(self):

        self.vector_service = VectorService()

    def process_document(
        self,
        file
    ):

        document_id = str(uuid.uuid4())

        file_path = FileService.save_file(file)

        pdf = PDFService.extract_text(file_path)

        chunks = ChunkService.chunk_text(
            pdf["text"]
        )

        embeddings = EmbeddingService.generate_embeddings(
            chunks,
            metadata={
                "filename": file.filename,
                "document_id": document_id
            }
        )

        self.vector_service.add_embeddings(
            embeddings
        )

        return {
            "document_id": document_id,
            "filename": file.filename,
            "pages": pdf["pages"],
            "total_chunks": len(chunks),
            "status": "Processed"
        }