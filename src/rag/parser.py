def parse_markdown_sections(
    markdown_content: str
):
    if not markdown_content:
        return {}

    sections = {}
    current_section = "overview"
    sections[current_section] = []

    for line in markdown_content.splitlines():
        line = line.strip()

        if line.startswith("## "):
            current_section = (
                line.replace("## ", "")
                .strip()
                .lower()
            )

            sections[current_section] = []

            continue

        if line and not line.startswith("#"):
            sections[current_section].append(
                line
            )

    return {
        section: " ".join(content)
        for section, content
        in sections.items()
    }