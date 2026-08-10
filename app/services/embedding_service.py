from sentence_transformers import SentenceTransformer


class EmbeddingService:

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    @classmethod
    def generate_embeddings(
        cls,
        chunks,
        metadata=None
    ):

        embeddings = []

        metadata = metadata or {}

        for chunk in chunks:

            vector = cls.model.encode(
                chunk["text"]
            )

            embeddings.append({

                "chunk_id": chunk["chunk_id"],

                "text": chunk["text"],

                "embedding": vector.tolist(),

                "metadata": metadata

            })

        return embeddings