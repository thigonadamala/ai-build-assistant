from src.rag_service import get_champion_context


context = get_champion_context(
    "Ahri"
)

print(context)