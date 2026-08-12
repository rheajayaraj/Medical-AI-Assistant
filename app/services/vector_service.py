import chromadb


class VectorService:

    def __init__(self):

        self.client = chromadb.PersistentClient(
            path="vector_store"
        )

        self.collection = self.client.get_or_create_collection(
            name="medical_documents"
        )

    def add_embeddings(
        self,
        embeddings
    ):
        for item in embeddings:

            self.collection.add(

                ids=[
                    item["chunk_id"]
                ],

                documents=[
                    item["text"]
                ],

                embeddings=[
                    item["embedding"]
                ],

                metadatas=[
                    item.get("metadata", {})
                ]
            )

    def search(
    self,
    query_embedding,
    top_k=3
    ):

        return self.collection.query(

            query_embeddings=[
                query_embedding
            ],

            n_results=top_k,

            include=[
                "documents",
                "metadatas",
                "distances"
            ]

        )

    def document_exists(
    self,
    file_hash: str
    ):

        results = self.collection.get(
            where={
                "file_hash": file_hash
            }
        )

        return len(results["ids"]) > 0