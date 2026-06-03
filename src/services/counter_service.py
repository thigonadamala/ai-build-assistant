from src.database.db import get_connection

def get_counters(champion=None, role=None, limit=3):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT
                id,
                champion,
                counter_champion,
                role,
                winrate
            FROM lol_counters
            WHERE 1 = 1
        """

        params = {}

        if champion:
            query += " AND LOWER(champion) = LOWER(:champion)"
            params["champion"] = champion.strip()

        if role:
            query += " AND LOWER(role) = LOWER(:role)"
            params["role"] = role.strip()

        query += " ORDER BY winrate ASC FETCH FIRST :limit ROWS ONLY"
        params["limit"] = limit

        cursor.execute(query, params)

        rows = cursor.fetchall()

        counters = []

        for row in rows:
            counters.append({
                "id": row[0],
                "champion": row[1],
                "counter_champion": row[2],
                "role": row[3],
                "winrate": row[4]
            })

        return {
            "total": len(counters),
            "filters": {
                "champion": champion,
                "role": role,
                "limit": limit
            },
            "data": counters
        }

    except Exception as e:
        return {
            "error": str(e),
            "total": 0,
            "filters": {
                "champion": champion,
                "role": role,
                "limit": limit
            },
            "data": []
        }

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()  