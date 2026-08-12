import uuid

from app.services.file_service import FileService
from app.services.pdf_service import PDFService
from app.services.chunk_service import ChunkService
from app.services.embedding_service import EmbeddingService
from app.services.vector_service import VectorService
from app.services.hash_service import HashService


class DocumentService:

    def __init__(self):

        self.vector_service = VectorService()

    def process_document(
        self,
        file
    ):

        document_id = str(uuid.uuid4())

        file_path = FileService.save_file(file)

        file_hash = HashService.generate_file_hash(
            file_path
        )

        if self.vector_service.document_exists(file_hash):

            return {
                "document_id": None,
                "filename": file.filename,
                "pages": 0,
                "total_chunks": 0,
                "status": "Duplicate document"
            }

        pages  = PDFService.extract_text(file_path)

        chunks = ChunkService.chunk_pages(
            pages 
        )

        embeddings = []

        for chunk in chunks:

            embedding = EmbeddingService.generate_embedding(
                chunk["text"]
            )

            embeddings.append({

                "chunk_id": chunk["chunk_id"],

                "text": chunk["text"],

                "embedding": embedding,

                "metadata": {

                    "filename": file.filename,

                    "document_id": document_id,

                    "page": chunk["page"],

                    "chunk_index": chunk["chunk_index"],

                    "file_hash": file_hash

                }

            })

        self.vector_service.add_embeddings(
            embeddings
        )

        return {
            "document_id": document_id,
            "filename": file.filename,
            "pages": len(pages),
            "total_chunks": len(chunks),
            "status": "Processed"
        }