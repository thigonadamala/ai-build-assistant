def interpret_question(question: str, available_champions: list[str]):
    question_lower = question.lower()

    champion = None
    role = None
    limit = 1
    intent = "general"

    # Detecta intenção da pergunta
    if "winrate" in question_lower or "taxa de vitória" in question_lower:
        intent = "winrate"

    elif "build" in question_lower or "item" in question_lower:
        intent = "build"

    # Detecta campeão citado na pergunta
    for available_champion in available_champions:
        if available_champion.lower() in question_lower:
            champion = available_champion
            break

    # Detecta rota citada na pergunta
    if "mid" in question_lower:
        role = "mid"

    elif "adc" in question_lower:
        role = "adc"

    elif "support" in question_lower:
        role = "support"

    return {
        "intent": intent,
        "champion": champion,
        "role": role,
        "limit": limit
    }