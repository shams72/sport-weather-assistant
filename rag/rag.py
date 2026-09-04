from pathlib import Path

import chromadb
from sentence_transformers import SentenceTransformer


DOCUMENTS_DIR = Path(__file__).parent / "documents"

model = SentenceTransformer("all-MiniLM-L6-v2")

client = chromadb.PersistentClient(
    path=str(Path(__file__).parent / "chroma_db")
)

collection = client.get_or_create_collection(
    name="sports"
)


def load_documents():
    documents = []
    ids = []

    for file in DOCUMENTS_DIR.glob("*.txt"):
        text = file.read_text(encoding="utf-8")

        documents.append(text)
        ids.append(file.stem)

    return documents, ids


def build_database():
    documents, ids = load_documents()

    embeddings = model.encode(documents).tolist()

    collection.upsert(
        documents=documents,
        embeddings=embeddings,
        ids=ids
    )

    print(f"Loaded {len(documents)} documents.")


def search(query: str, n_results: int = 3):
    query_embedding = model.encode([query]).tolist()

    results = collection.query(
        query_embeddings=query_embedding,
        n_results=n_results
    )

    return results["documents"][0]


if __name__ == "__main__":
    #build_database()

    results = search(
        "Can I run today?",
    )

    print("\nRelevant information:\n")

    for result in results:
        print(result)
        print("-" * 50)