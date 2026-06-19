from src.database.db import get_connection


def get_champions(
    champion: str | None = None,
    limit: int = 20
):
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        query = """
            SELECT
                riot_id,
                champion_key,
                name,
                title,
                primary_tag,
                secondary_tag,
                partype,
                version
            FROM LOL_CHAMPIONS
            WHERE 1 = 1
        """

        params = {}

        if champion:
            query += " AND LOWER(name) = LOWER(:champion)"
            params["champion"] = champion.strip()

        query += " ORDER BY name FETCH FIRST :limit ROWS ONLY"
        params["limit"] = limit

        cursor.execute(query, params)

        rows = cursor.fetchall()

        data = [
            {
                "riot_id": row[0],
                "champion_key": row[1],
                "name": row[2],
                "title": row[3],
                "primary_tag": row[4],
                "secondary_tag": row[5],
                "partype": row[6],
                "version": row[7]
            }
            for row in rows
        ]

        return {
            "total": len(data),
            "filters": {
                "champion": champion,
                "limit": limit
            },
            "data": data
        }

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()
