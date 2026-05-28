from fastapi import FastAPI

from src.build_service import get_builds
from src.orchestrator import handle_question

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
    return handle_question(question)