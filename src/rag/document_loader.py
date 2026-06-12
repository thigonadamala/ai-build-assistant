from pathlib import Path


KNOWLEDGE_ROOT = Path(
    "knowledge"
)


def read_markdown_file(
    file_path: Path
):
    knowledge_root = KNOWLEDGE_ROOT.resolve()
    resolved_file_path = file_path.resolve()

    if not resolved_file_path.is_relative_to(
        knowledge_root
    ):
        return None

    if not resolved_file_path.is_file():
        return None

    try:
        return resolved_file_path.read_text(
            encoding="utf-8"
        )

    except Exception as e:
        print(
            f"Erro ao ler arquivo "
            f"{file_path}: {e}"
        )

        return None


def load_champion_document(
    champion: str
):
    if not champion:
        return None

    champion_file = (
        KNOWLEDGE_ROOT /
        "champions" /
        f"{champion.lower()}.md"
    )

    return read_markdown_file(
        champion_file
    )


def load_guide_document(
    guide_name: str
):
    if not guide_name:
        return None

    guide_file = (
        KNOWLEDGE_ROOT /
        "guides" /
        f"{guide_name}.md"
    )

    return read_markdown_file(
        guide_file
    )
