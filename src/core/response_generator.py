from src.ai.llm_service import generate_llm_answer

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


def get_section(data, source_name, section_name):
    rag_context = data.get("rag_context", {})
    source = rag_context.get(source_name, {})
    sections = source.get("sections", {})

    return sections.get(section_name)


def has_reliable_overview_context(data):
    build = data.get("build", [])
    runes = data.get("runes", [])
    counters = data.get("counters", [])

    champion_overview = get_section(
        data=data,
        source_name="champion",
        section_name="overview"
    )

    return bool(
        build or
        runes or
        counters or
        champion_overview
    )


def generate_overview_answer(data):
    champion = data["champion"]

    if not has_reliable_overview_context(data):
        return (
            f"Não encontrei dados suficientes para gerar "
            f"uma visão geral confiável sobre {champion}."
        )

    build = data["build"][0] if data["build"] else None
    rune = data["runes"][0] if data["runes"] else None
    counters = data["counters"]

    champion_overview = get_section(
        data=data,
        source_name="champion",
        section_name="overview"
    )

    champion_playstyle = get_section(
        data=data,
        source_name="champion",
        section_name="estilo de jogo"
    )

    champion_strengths = get_section(
        data=data,
        source_name="champion",
        section_name="pontos fortes"
    )

    champion_weaknesses = get_section(
        data=data,
        source_name="champion",
        section_name="pontos fracos"
    )

    guide_overview = get_section(
        data=data,
        source_name="guide",
        section_name="overview"
    )

    guide_roaming = get_section(
        data=data,
        source_name="guide",
        section_name="quando fazer roaming"
    )

    prompt = f"""
    Você é um assistente estratégico de League of Legends.

    Gere uma resposta natural, objetiva e útil sobre o campeão abaixo.

    Regras:
    - Responda em português.
    - Não invente dados.
    - Use apenas as informações fornecidas.
    - Seja direto.
    - Não use markdown.
    - Não cite JSON.
    - Não diga que está usando contexto.
    - Se algum dado estiver ausente, ignore esse dado.
    - Se não houver dados específicos do campeão, informe que não há dados suficientes.

    Campeão:
    {champion}

    Dados de build:
    {build}

    Dados de runas:
    {rune}

    Dados de counters:
    {counters}

    Contexto geral do campeão:
    {champion_overview}

    Estilo de jogo:
    {champion_playstyle}

    Pontos fortes:
    {champion_strengths}

    Pontos fracos:
    {champion_weaknesses}

    Contexto geral de roaming:
    {guide_overview}

    Dicas de roaming:
    {guide_roaming}
    """

    return generate_llm_answer(
        prompt=prompt
    )


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