def generate_winrate_answer(data):
    return (
        f"O winrate encontrado para "
        f"{data['champion']} "
        f"na rota {data['role']} "
        f"é de {data['winrate']}%."
    )


def generate_build_answer(data):
    return (
        f"A melhor build encontrada para "
        f"{data['champion']} "
        f"na rota {data['role']} "
        f"usa {data['item']}, "
        f"com winrate de "
        f"{data['winrate']}%."
    )


def generate_counters_answer(data):
    if not data:
        return "Não encontrei counters para essa pergunta."

    champion = data[0]["champion"]
    counter_names = [
        counter["counter_champion"]
        for counter in data
    ]

    counters_text = ", ".join(counter_names)

    return (
        f"Os principais counters de "
        f"{champion} "
        f"são {counters_text}."
    )


def generate_runes_answer(data):
    if not data:
        return "Não encontrei runas para essa pergunta."

    best_rune = data[0]

    return (
        f"A melhor página de runas encontrada para "
        f"{best_rune['champion']} "
        f"na rota {best_rune['role']} "
        f"usa {best_rune['primary_rune']} "
        f"com {best_rune['secondary_rune']}, "
        f"com winrate de {best_rune['winrate']}%."
    )


def extract_first_context_paragraph(context: str | None):
    if not context:
        return None

    paragraphs = [
        paragraph.strip()
        for paragraph in context.split("\n\n")
        if paragraph.strip()
    ]

    for paragraph in paragraphs:
        if not paragraph.startswith("#"):
            return paragraph.rstrip(".")

    return None


def generate_overview_answer(data):
    champion = data["champion"]

    build = data["build"][0] if data["build"] else None
    rune = data["runes"][0] if data["runes"] else None
    counters = data["counters"]
    knowledge_context = data.get("knowledge_context")

    context_summary = extract_first_context_paragraph(
        knowledge_context
    )

    answer_parts = []

    if context_summary:
        answer_parts.append(context_summary)

    if build:
        answer_parts.append(
            f"a build recomendada usa {build['item']} "
            f"na rota {build['role']} "
            f"com winrate de {build['winrate']}%"
        )

    if rune:
        answer_parts.append(
            f"a página de runas usa {rune['primary_rune']} "
            f"com {rune['secondary_rune']} "
            f"e winrate de {rune['winrate']}%"
        )

    if counters:
        counter_names = [
            counter["counter_champion"]
            for counter in counters
        ]

        counters_text = ", ".join(counter_names)

        answer_parts.append(
            f"os principais counters são {counters_text}"
        )

    if not answer_parts:
        return f"Não encontrei dados suficientes para gerar uma visão geral de {champion}."

    overview_text = ". ".join(answer_parts)

    return f"Visão geral de {champion}: {overview_text}."


ANSWER_GENERATORS = {
    "winrate": generate_winrate_answer,
    "build": generate_build_answer,
    "counters": generate_counters_answer,
    "runes": generate_runes_answer,
    "overview": generate_overview_answer
}


def generate_answer(intent: str, data):
    generator = ANSWER_GENERATORS.get(intent)

    if not generator:
        return "Ainda não sei responder esse tipo de pergunta."

    return generator(data)