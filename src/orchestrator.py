from src.build_service import get_builds
from src.counter_service import get_counters
from src.llm_service import ask_llm
from src.response_generator import generate_answer
from src.rune_service import get_runes


DEFAULT_LIMITS = {
    "build": 1,
    "winrate": 1,
    "counters": 3,
    "runes": 3,
    "matchup": 3,
    "skills": 3,
    "synergies": 3,
    "power_spike": 1,
    "general": 1
}


MAX_LIMITS = {
    "build": 5,
    "winrate": 5,
    "counters": 10,
    "runes": 10,
    "matchup": 10,
    "skills": 10,
    "synergies": 10,
    "power_spike": 5,
    "general": 10
}


INTENT_CONFIG = {
    "counters": {
        "service": get_counters,
        "empty_message": "Não encontrei counters para essa pergunta.",
        "response_mode": "list"
    },
    "runes": {
        "service": get_runes,
        "empty_message": "Não encontrei runas para essa pergunta.",
        "response_mode": "list"
    }
}


def resolve_limit(intent: str, filters: dict) -> int:
    requested_limit = filters.get("limit")

    default_limit = DEFAULT_LIMITS.get(intent, 1)
    max_limit = MAX_LIMITS.get(intent, 10)

    if requested_limit is None:
        return default_limit

    try:
        requested_limit = int(requested_limit)

    except (ValueError, TypeError):
        return default_limit

    if requested_limit <= 0:
        return default_limit

    if requested_limit > max_limit:
        return max_limit

    return requested_limit


def build_response(
    question: str,
    interpreted_filters: dict,
    applied_filters: dict | None,
    total: int | None,
    answer: str,
    data: list
):
    response = {
        "question": question,
        "interpreted_filters": interpreted_filters,
        "answer": answer,
        "data": data
    }

    if applied_filters is not None:
        response["applied_filters"] = applied_filters

    if total is not None:
        response["total"] = total

    return response


def handle_build_intent(
    question: str,
    filters: dict,
    champion: str | None,
    role: str | None,
    limit: int
):
    result = get_builds(
        champion=champion,
        role=role,
        limit=limit
    )

    data = result["data"]

    if not data:
        return build_response(
            question=question,
            interpreted_filters=filters,
            applied_filters=None,
            total=None,
            answer="Não encontrei builds para essa pergunta.",
            data=[]
        )

    answer = generate_answer(
        intent="build",
        data=data[0]
    )

    return build_response(
        question=question,
        interpreted_filters=filters,
        applied_filters=None,
        total=None,
        answer=answer,
        data=data
    )


def handle_configured_intent(
    question: str,
    filters: dict,
    intent: str,
    champion: str | None,
    role: str | None,
    limit: int
):
    config = INTENT_CONFIG[intent]
    service = config["service"]

    result = service(
        champion=champion,
        role=role,
        limit=limit
    )

    total = result["total"]
    service_filters = result["filters"]
    data = result["data"]

    if not data:
        return build_response(
            question=question,
            interpreted_filters=filters,
            applied_filters=service_filters,
            total=total,
            answer=config["empty_message"],
            data=[]
        )

    answer = generate_answer(
        intent=intent,
        data=data
    )

    return build_response(
        question=question,
        interpreted_filters=filters,
        applied_filters=service_filters,
        total=total,
        answer=answer,
        data=data
    )


def handle_question(question: str):
    filters = ask_llm(question)

    print("FILTROS LLM:")
    print(filters)

    intent = filters.get("intent", "general")
    champion = filters.get("champion")
    role = filters.get("role")
    limit = resolve_limit(intent, filters)

    filters["limit"] = limit

    if intent == "build":
        return handle_build_intent(
            question=question,
            filters=filters,
            champion=champion,
            role=role,
            limit=limit
        )

    if intent in INTENT_CONFIG:
        return handle_configured_intent(
            question=question,
            filters=filters,
            intent=intent,
            champion=champion,
            role=role,
            limit=limit
        )

    if intent == "matchup":
        return build_response(
            question=question,
            interpreted_filters=filters,
            applied_filters=None,
            total=None,
            answer="Sistema de matchups ainda não implementado.",
            data=[]
        )

    return build_response(
        question=question,
        interpreted_filters=filters,
        applied_filters=None,
        total=None,
        answer="Ainda não sei responder esse tipo de pergunta.",
        data=[]
    )