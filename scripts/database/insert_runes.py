from src.database.db import get_connection


def insert_runes():
    connection = None
    cursor = None

    runes = [
        ("Ahri", "mid", "Eletrocutar", "Precisão", 52.3),
        ("Zed", "mid", "Conquistador", "Dominação", 49.8),
        ("Jinx", "adc", "Ritmo Fatal", "Precisão", 51.2)
    ]

    try:
        connection = get_connection()

        cursor = connection.cursor()

        cursor.executemany("""
            INSERT INTO lol_runes (
                champion,
                role,
                primary_rune,
                secondary_rune,
                winrate
            )
            VALUES (
                :1,
                :2,
                :3,
                :4,
                :5
            )
        """, runes)

        connection.commit()

        print("Runas inseridas com sucesso!")

    except Exception as e:
        print("Erro ao inserir runas:")
        print(e)

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


if __name__ == "__main__":
    insert_runes()