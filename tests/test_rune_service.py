from src.services.rune_service import get_runes

result = get_runes(
    champion="Ahri",
    role="mid",
    limit=3
)

print(result)