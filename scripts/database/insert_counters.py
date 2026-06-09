from src.database.db import get_connection


def insert_counters():
    connection = None
    cursor = None

    counters = [
        ("Ahri", "Zed", "mid", 48.2),
        ("Ahri", "Fizz", "mid", 47.1),
        ("Ahri", "Kassadin", "mid", 46.5)
    ]

    try:
        connection = get_connection()

        cursor = connection.cursor()

        cursor.executemany("""
            INSERT INTO lol_counters (
                champion,
                counter_champion,
                role,
                winrate
            )
            VALUES (
                :1,
                :2,
                :3,
                :4
            )
        """, counters)

        connection.commit()

        print("Counters inseridos com sucesso!")

    except Exception as e:
        print("Erro ao inserir counters:")
        print(e)

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


if __name__ == "__main__":
    insert_counters()