from src.rag.document_loader import (
    load_champion_document,
    load_guide_document
)

from src.rag.parser import parse_markdown_sections


def retrieve_champion_context(
    champion: str
):
    champion_document = load_champion_document(
        champion=champion
    )

    champion_sections = parse_markdown_sections(
        champion_document
    )

    return {
        "raw_content": champion_document,
        "sections": champion_sections
    }


def retrieve_guide_context(
    guide_name: str
):
    guide_document = load_guide_document(
        guide_name=guide_name
    )

    guide_sections = parse_markdown_sections(
        guide_document
    )

    return {
        "raw_content": guide_document,
        "sections": guide_sections
    }


def retrieve_overview_context(
    champion: str
):
    champion_context = retrieve_champion_context(
        champion=champion
    )

    guide_context = retrieve_guide_context(
        guide_name="mid_lane_roaming"
    )

    return {
        "champion": champion_context,
        "guide": guide_context
    }