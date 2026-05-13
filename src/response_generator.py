def generate_answer(intent: str, best_build: dict):
    # Gera resposta focada em winrate
    if intent == "winrate":
        return (
            f"O winrate encontrado para "
            f"{best_build['champion']} "
            f"na rota {best_build['role']} "
            f"é de {best_build['winrate']}%."
        )

    # Gera resposta focada em build
    if intent == "build":
        return (
            f"A melhor build encontrada para "
            f"{best_build['champion']} "
            f"na rota {best_build['role']} "
            f"usa {best_build['item']}, "
            f"com winrate de "
            f"{best_build['winrate']}%."
        )

    # Resposta geral quando a intenção não é específica
    return (
        f"Encontrei dados para "
        f"{best_build['champion']} "
        f"na rota {best_build['role']}. "
        f"O item recomendado é "
        f"{best_build['item']} "
        f"e o winrate é "
        f"{best_build['winrate']}%."
    )