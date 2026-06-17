from src.ai.embedding_service import generate_embedding


def build_embedding_text(chunk: dict) -> str:
    source = chunk.get("source", "")
    source_type = chunk.get("source_type", "")
    section = chunk.get("section", "")
    text = chunk.get("text", "")

    return (
        f"Fonte: {source}. "
        f"Tipo: {source_type}. "
        f"Seção: {section}. "
        f"Conteúdo: {text}"
    ).strip()


def add_embeddings_to_chunks(chunks: list[dict]) -> list[dict]:
    indexed_chunks = []

    for chunk in chunks:
        embedding_text = build_embedding_text(chunk)

        embedding = generate_embedding(
            embedding_text
        )

        indexed_chunks.append(
            {
                **chunk,
                "embedding": embedding
            }
        )

    return indexed_chunks