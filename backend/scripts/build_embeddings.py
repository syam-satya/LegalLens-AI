import sys
from pathlib import Path
from uuid import uuid4

ROOT_DIR = Path(__file__).resolve().parent.parent
sys.path.append(str(ROOT_DIR))

from app.db.chroma import rules_collection
from app.services.chunk_service import ChunkService
from app.services.embedding_service import EmbeddingService
from app.services.government_rule_service import GovernmentRuleService


def main():

    embedder = EmbeddingService()

    documents = GovernmentRuleService.load_rule_files()

    for document in documents:

        chunks = ChunkService.create_chunks(
            document["content"]
        )

        for chunk in chunks:

            embedding = embedder.generate_embedding(
                chunk
            )

            rules_collection.add(
                ids=[str(uuid4())],
                documents=[chunk],
                embeddings=[embedding],
                metadatas=[
                    {
                        "source":
                        document["filename"]
                    }
                ]
            )

    print("Embedding build complete.")


if __name__ == "__main__":
    main()