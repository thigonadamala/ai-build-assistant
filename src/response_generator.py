def generate_answer(intent: str, data):
    # Resposta para winrate
    if intent == "winrate":
        return (
            f"O winrate encontrado para "
            f"{data['champion']} "
            f"na rota {data['role']} "
            f"é de {data['winrate']}%."
        )

    # Resposta para build
    if intent == "build":
        return (
            f"A melhor build encontrada para "
            f"{data['champion']} "
            f"na rota {data['role']} "
            f"usa {data['item']}, "
            f"com winrate de "
            f"{data['winrate']}%."
        )

    # Resposta para counters
    if intent == "counters":
        champion = data[0]["champion"]

        return (
            f"Encontrei {len(data)} counter(s) "
            f"para {champion}."
        )

    # Resposta geral
    return "Encontrei dados para sua pergunta."     