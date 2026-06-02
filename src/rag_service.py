from pathlib import Path


KNOWLEDGE_PATH = Path("knowledge/champions")


def get_champion_context(champion: str):
    if not champion:
        return None

    champion_file = (
        KNOWLEDGE_PATH /
        f"{champion.lower()}.md"
    )

    if not champion_file.exists():
        return None

    try:
        return champion_file.read_text(
            encoding="utf-8"
        )

    except Exception as e:
        print(
            f"Erro ao ler contexto de {champion}: {e}"
        )
        return None