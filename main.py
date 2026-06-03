from fastapi import FastAPI
from src.services.build_service import get_builds
from src.observability.stats_service import get_stats
from src.core.orchestrator import handle_question

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


@app.get("/stats")
def stats():
    return get_stats()