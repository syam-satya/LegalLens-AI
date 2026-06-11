import chromadb

from app.config.settings import settings


client = chromadb.PersistentClient(
    path=settings.CHROMA_DB_PATH
)

rules_collection = client.get_or_create_collection(
    name="government_rules"
)