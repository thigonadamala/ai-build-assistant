from src.database.db import get_connection


def get_available_champions():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        # Busca campeões únicos cadastrados no banco
        cursor.execute("SELECT DISTINCT champion FROM lol_builds")

        rows = cursor.fetchall()

        # Retorna lista simples
        return [row[0] for row in rows]

    except Exception:
        return []

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


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

        # Filtro por champion
        if champion:
            sql += " AND LOWER(champion) = LOWER(:champion)"
            params["champion"] = champion.strip()

        # Filtro por role
        if role:
            sql += " AND LOWER(role) = LOWER(:role)"
            params["role"] = role.strip()

        # Ordena pelo maior winrate
        sql += " ORDER BY winrate DESC"

        # Limita resultados
        if limit:
            sql = f"""
                SELECT *
                FROM ({sql})
                WHERE ROWNUM <= :limit
            """

            params["limit"] = limit

        cursor.execute(sql, params)

        rows = cursor.fetchall()

        # Converte resultado SQL em JSON
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