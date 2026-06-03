from src.database.db import get_connection

def get_runes(champion=None, role=None, limit=3):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT
                id,
                champion,
                role,
                primary_rune,
                secondary_rune,
                winrate
            FROM lol_runes
            WHERE 1 = 1
        """

        params = {}

        if champion:
            query += " AND LOWER(champion) = LOWER(:champion)"
            params["champion"] = champion

        if role:
            query += " AND LOWER(role) = LOWER(:role)"
            params["role"] = role

        query += " ORDER BY winrate DESC FETCH FIRST :limit ROWS ONLY"
        params["limit"] = limit

        cursor.execute(query, params)

        rows = cursor.fetchall()

        runes = []

        for row in rows:
            runes.append({
                "id": row[0],
                "champion": row[1],
                "role": row[2],
                "primary_rune": row[3],
                "secondary_rune": row[4],
                "winrate": row[5]
            })

        return {
            "total": len(runes),
            "filters": {
                "champion": champion,
                "role": role,
                "limit": limit
            },
            "data": runes
        }

    except Exception as e:
        return {
            "error": str(e),
            "data": []
        }

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()