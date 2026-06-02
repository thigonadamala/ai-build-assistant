from src.rag.rag_service import (
    get_rag_context
)


context = get_rag_context(
    "Ahri"
)

print(context)