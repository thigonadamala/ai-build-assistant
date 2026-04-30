from fastapi import FastAPI
from src.db import get_connection

app = FastAPI()


@app.get("/")
def home():
    return {"message": "API LoL funcionando"}


def get_available_champions():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Busca os campeões disponíveis no banco
        cursor.execute("SELECT DISTINCT champion FROM lol_builds")

        rows = cursor.fetchall()

        # Retorna os campeões em uma lista simples
        return [row[0] for row in rows]

    except Exception:
        return []

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


@app.get("/builds")
def get_builds(
    champion: str | None = None,
    role: str | None = None,
    limit: int | None = None
):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Query base
        sql = """
            SELECT champion, role, item, winrate
            FROM lol_builds
            WHERE 1 = 1
        """

        params = {}

        # Filtro por campeão
        if champion:
            sql += " AND LOWER(champion) = LOWER(:champion)"
            params["champion"] = champion.strip()

        # Filtro por rota
        if role:
            sql += " AND LOWER(role) = LOWER(:role)"
            params["role"] = role.strip()

        # Ordena pelo maior winrate
        sql += " ORDER BY winrate DESC"

        # Limita a quantidade de resultados
        if limit:
            sql = f"""
                SELECT *
                FROM ({sql})
                WHERE ROWNUM <= :limit
            """
            params["limit"] = limit

        cursor.execute(sql, params)

        rows = cursor.fetchall()

        # Converte os dados do banco em JSON
        result = [
            {
                "champion": row[0],
                "role": row[1],
                "item": row[2],
                "winrate": row[3]
            }
            for row in rows
        ]

        return {
            "total": len(result),
            "filters": {
                "champion": champion,
                "role": role,
                "limit": limit
            },
            "data": result
        }

    except Exception as e:
        return {"error": str(e)}

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


@app.get("/ask")
def ask(question: str):
    question_lower = question.lower()

    champion = None
    role = None
    limit = 1

    # Busca campeões existentes no banco
    available_champions = get_available_champions()

    # Detecta automaticamente se algum campeão aparece na pergunta
    for available_champion in available_champions:
        if available_champion.lower() in question_lower:
            champion = available_champion
            break

    # Detecta a rota mencionada na pergunta
    if "mid" in question_lower:
        role = "mid"
    elif "adc" in question_lower:
        role = "adc"
    elif "support" in question_lower:
        role = "support"

    # Consulta os dados usando os filtros interpretados
    result = get_builds(champion=champion, role=role, limit=limit)

    data = result["data"]

    if not data:
        return {
            "question": question,
            "interpreted_filters": {
                "champion": champion,
                "role": role,
                "limit": limit
            },
            "answer": "Não encontrei dados para essa pergunta.",
            "data": []
        }

    best_build = data[0]

    # Monta resposta em linguagem natural
    answer = (
        f"A melhor build encontrada foi para {best_build['champion']} "
        f"na rota {best_build['role']}, usando {best_build['item']}, "
        f"com winrate de {best_build['winrate']}%."
    )

    return {
        "question": question,
        "interpreted_filters": {
            "champion": champion,
            "role": role,
            "limit": limit
        },
        "answer": answer,
        "data": data
    }