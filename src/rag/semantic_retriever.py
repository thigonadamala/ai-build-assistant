from src.ai.embedding_service import generate_embedding
from src.rag.similarity import cosine_similarity


def retrieve_top_k_chunks(
    question: str,
    indexed_chunks: list[dict],
    top_k: int = 3
) -> list[dict]:
    if not question or not question.strip():
        return []

    if not indexed_chunks:
        return []

    question_embedding = generate_embedding(question)

    scored_chunks = []

    for chunk in indexed_chunks:
        chunk_embedding = chunk.get("embedding", [])

        score = cosine_similarity(
            question_embedding,
            chunk_embedding
        )

        scored_chunks.append(
            {
                **chunk,
                "score": score
            }
        )

    scored_chunks.sort(
        key=lambda chunk: chunk["score"],
        reverse=True
    )

    return scored_chunks[:top_k]