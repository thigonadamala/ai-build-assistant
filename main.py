from fastapi import FastAPI
from src.build_service import get_builds
from src.llm_service import ask_llm
from src.response_generator import generate_answer

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API LoL funcionando"}


@app.get("/builds")
def builds(
    champion: str | None = None,
    role: str | None = None,
    limit: int | None = None
):
    return get_builds(
        champion=champion,
        role=role,
        limit=limit
    )


@app.get("/ask")
def ask(question: str):

    filters = ask_llm(question)

    print("FILTROS LLM:")
    print(filters)

    intent = filters.get("intent", "general")
    champion = filters.get("champion")
    role = filters.get("role")
    limit = filters.get("limit", 1)

    if intent == "build":

        result = get_builds(
            champion=champion,
            role=role,
            limit=limit
        )

        data = result["data"]

        if not data:
            return {
                "question": question,
                "interpreted_filters": filters,
                "answer": "Não encontrei builds para essa pergunta.",
                "data": []
            }

        answer = generate_answer(
            intent=intent,
            best_build=data[0]
        )

        return {
            "question": question,
            "interpreted_filters": filters,
            "answer": answer,
            "data": data
        }

    elif intent == "runes":

        return {
            "question": question,
            "interpreted_filters": filters,
            "answer": "Sistema de runas ainda não implementado."
        }

    elif intent == "counters":

        return {
            "question": question,
            "interpreted_filters": filters,
            "answer": "Sistema de counters ainda não implementado."
        }

    elif intent == "matchup":

        return {
            "question": question,
            "interpreted_filters": filters,
            "answer": "Sistema de matchups ainda não implementado."
        }

    else:

        return {
            "question": question,
            "interpreted_filters": filters,
            "answer": "Ainda não sei responder esse tipo de pergunta."
        }