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

    if "limit" not in filters:
        filters["limit"] = 1

    result = get_builds(
        champion=filters["champion"],
        role=filters["role"],
        limit=filters["limit"]
    )

    print("RESULTADO DO BANCO:")
    print(result)

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