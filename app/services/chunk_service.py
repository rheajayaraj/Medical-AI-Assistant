class ChunkService:

    @staticmethod
    def chunk_text(
        text: str,
        chunk_size: int = 500
    ):
        """
        Split text into fixed-size chunks.
        """

        chunks = []

        start = 0
        chunk_id = 1

        while start < len(text):

            end = start + chunk_size

            chunks.append({
                "chunk_id": chunk_id,
                "text": text[start:end]
            })

            chunk_id += 1

            start = end

        return chunks