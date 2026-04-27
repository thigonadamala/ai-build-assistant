from fastapi import FastAPI
from src.db import get_connection

app = FastAPI()

@app.get("/")
def home():
    return {"message": "API LoL funcionando"}

@app.get("/builds")
def get_builds():
    connection = None
    cursor = None

    try:
        # Abre conexão com o banco
        connection = get_connection()
        cursor = connection.cursor()

        # Consulta dados da tabela lol_builds
        cursor.execute("SELECT champion, role, item, winrate FROM lol_builds")

        # Captura os resultados
        rows = cursor.fetchall()

        # Converte para lista de dicionários (JSON)
        result = []
        for row in rows:
            result.append({
                "champion": row[0],
                "role": row[1],
                "item": row[2],
                "winrate": row[3]
            })

        return result

    except Exception as e:
        return {"error": str(e)}

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()