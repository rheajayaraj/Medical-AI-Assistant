import uuid


class ChunkService:

    @staticmethod
    def chunk_text(
        text: str,
        chunk_size: int = 500
    ):

        chunks = []

        start = 0

        while start < len(text):

            end = start + chunk_size

            chunks.append({
                "chunk_id": str(uuid.uuid4()),
                "text": text[start:end]
            })

            start = end

        return chunks