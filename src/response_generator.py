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

    # Resposta para runas
    if intent == "runes":
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

    # Resposta geral
    return "Ainda não sei responder esse tipo de pergunta."