from fastapi import FastAPI

from src.build_service import get_available_champions, get_builds
from src.interpretation import interpret_question
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
    available_champions = get_available_champions()

    filters = interpret_question(
        question=question,
        available_champions=available_champions
    )

    result = get_builds(
        champion=filters["champion"],
        role=filters["role"],
        limit=filters["limit"]
    )

    data = result["data"]

    if not data:
        return {
            "question": question,
            "interpreted_filters": filters,
            "answer": "Não encontrei dados para essa pergunta.",
            "data": []
        }

    answer = generate_answer(
        intent=filters["intent"],
        best_build=data[0]
    )

    return {
        "question": question,
        "interpreted_filters": filters,
        "answer": answer,
        "data": data
    }