from sentence_transformers import SentenceTransformer


class EmbeddingService:

    model = SentenceTransformer(
        "all-MiniLM-L6-v2"
    )

    @classmethod
    def generate_embedding(
        cls,
        text: str
    ):

        return cls.model.encode(
            text
        ).tolist()

    @classmethod
    def generate_embeddings(
        cls,
        chunks,
        metadata=None
    ):

        metadata = metadata or {}

        embeddings = []

        for chunk in chunks:

            embeddings.append({

                "chunk_id": chunk["chunk_id"],

                "text": chunk["text"],

                "embedding": cls.generate_embedding(
                    chunk["text"]
                ),

                "metadata": metadata

            })

        return embeddings