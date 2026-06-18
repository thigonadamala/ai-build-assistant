from src.database.db import get_connection


MERGE_CHAMPION_SQL = """
MERGE INTO LOL_CHAMPIONS target
USING (
    SELECT
        :riot_id AS riot_id,
        :champion_key AS champion_key,
        :name AS name,
        :title AS title,
        :primary_tag AS primary_tag,
        :secondary_tag AS secondary_tag,
        :partype AS partype,
        :version AS version
    FROM dual
) source
ON (
    target.riot_id = source.riot_id
)
WHEN MATCHED THEN
    UPDATE SET
        target.champion_key = source.champion_key,
        target.name = source.name,
        target.title = source.title,
        target.primary_tag = source.primary_tag,
        target.secondary_tag = source.secondary_tag,
        target.partype = source.partype,
        target.version = source.version,
        target.updated_at = CURRENT_TIMESTAMP
WHEN NOT MATCHED THEN
    INSERT (
        riot_id,
        champion_key,
        name,
        title,
        primary_tag,
        secondary_tag,
        partype,
        version
    )
    VALUES (
        source.riot_id,
        source.champion_key,
        source.name,
        source.title,
        source.primary_tag,
        source.secondary_tag,
        source.partype,
        source.version
    )
"""


def load_champions(champions: list[dict]) -> int:
    if not champions:
        return 0

    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.executemany(
            MERGE_CHAMPION_SQL,
            champions
        )

        connection.commit()

        print(
            f"Campeoes carregados no Oracle: {len(champions)}"
        )

        return len(champions)

    except Exception:
        if connection:
            connection.rollback()

        raise

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()
