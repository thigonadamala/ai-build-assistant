from src.rag import document_loader


def test_load_champion_document_rejects_path_outside_knowledge(
    monkeypatch,
    tmp_path
):
    knowledge_root = tmp_path / "knowledge"
    champions_dir = knowledge_root / "champions"
    champions_dir.mkdir(parents=True)

    outside_file = tmp_path / "outside.md"
    outside_file.write_text(
        "conteudo fora de knowledge",
        encoding="utf-8"
    )

    monkeypatch.setattr(
        document_loader,
        "KNOWLEDGE_ROOT",
        knowledge_root
    )

    content = document_loader.load_champion_document(
        "../../outside"
    )

    assert content is None
