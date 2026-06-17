from src.rag.chunk_builder import build_chunks_from_sections
from src.rag.chunk_indexer import add_embeddings_to_chunks
from src.rag.retriever import retrieve_overview_context
from src.rag.semantic_retriever import retrieve_top_k_chunks


def build_chunks_from_overview_context(
    rag_context: dict
) -> list[dict]:
    chunks = []

    champion_context = rag_context.get("champion", {})
    champion_sections = champion_context.get("sections", {})

    guide_context = rag_context.get("guide", {})
    guide_sections = guide_context.get("sections", {})

    chunks.extend(
        build_chunks_from_sections(
            source="champion",
            source_type="champion",
            sections=champion_sections
        )
    )

    chunks.extend(
        build_chunks_from_sections(
            source="mid_lane_roaming",
            source_type="guide",
            sections=guide_sections
        )
    )

    return chunks


def remove_embeddings_from_chunks(
    chunks: list[dict]
) -> list[dict]:
    return [
        {
            key: value
            for key, value in chunk.items()
            if key != "embedding"
        }
        for chunk in chunks
    ]


def get_rag_context(
    champion: str,
    question: str | None = None
):
    if not champion:
        return {}

    rag_context = retrieve_overview_context(
        champion=champion
    )

    chunks = build_chunks_from_overview_context(
        rag_context=rag_context
    )

    if not question:
        rag_context["relevant_chunks"] = chunks
        return rag_context

    indexed_chunks = add_embeddings_to_chunks(
        chunks=chunks
    )

    relevant_chunks = retrieve_top_k_chunks(
        question=question,
        indexed_chunks=indexed_chunks,
        top_k=3
    )

    rag_context["relevant_chunks"] = remove_embeddings_from_chunks(
        chunks=relevant_chunks
    )

    return rag_context