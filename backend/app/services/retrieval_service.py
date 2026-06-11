from app.db.chroma import (
    rules_collection
)

from app.services.embedding_service import (
    EmbeddingService
)


class RetrievalService:

    def __init__(self):

        self.embedder = (
            EmbeddingService()
        )

    def retrieve(
        self,
        query: str,
        top_k: int = 5
    ):

        embedding = (
            self.embedder
            .generate_embedding(query)
        )

        results = (
            rules_collection.query(
                query_embeddings=[embedding],
                n_results=top_k
            )
        )

        return results