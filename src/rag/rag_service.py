from src.rag.retriever import (
    retrieve_overview_context
)


def get_rag_context(
    champion: str
):
    if not champion:
        return {}

    return retrieve_overview_context(
        champion=champion
    )