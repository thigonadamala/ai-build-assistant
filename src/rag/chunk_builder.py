def build_chunks_from_sections(
    source: str,
    source_type: str,
    sections: dict
) -> list[dict]:
    chunks = []

    for section_name, section_text in sections.items():
        if not section_text or not section_text.strip():
            continue

        chunks.append(
            {
                "source": source,
                "source_type": source_type,
                "section": section_name,
                "text": section_text
            }
        )

    return chunks