from src.rag import rag_service


def test_get_rag_context_without_question_skips_embeddings(
    monkeypatch
):
    base_context = {
        "champion": {
            "sections": {
                "overview": "Conteudo da campea."
            }
        },
        "guide": {
            "sections": {}
        }
    }

    monkeypatch.setattr(
        rag_service,
        "retrieve_overview_context",
        lambda champion: base_context
    )

    context = rag_service.get_rag_context(
        champion="Ahri"
    )

    assert context["relevant_chunks"] == [
        {
            "source": "champion",
            "source_type": "champion",
            "section": "overview",
            "text": "Conteudo da campea."
        }
    ]


def test_get_rag_context_returns_empty_without_champion():
    assert rag_service.get_rag_context(
        champion="",
        question="Como jogar?"
    ) == {}
