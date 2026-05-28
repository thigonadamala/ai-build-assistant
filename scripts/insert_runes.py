import os
import oracledb
from dotenv import load_dotenv

load_dotenv()


def insert_runes():
    connection = None
    cursor = None

    try:
        connection = oracledb.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dsn=os.getenv("DB_DSN")
        )

        cursor = connection.cursor()

        runes = [
            ("Ahri", "mid", "Eletrocutar", "Feitiçaria", 52.4),
            ("Jinx", "adc", "Ritmo Fatal", "Inspiração", 51.8),
            ("Lee Sin", "jungle", "Conquistador", "Inspiração", 50.9)
        ]

        cursor.executemany("""
            INSERT INTO lol_runes (
                champion,
                role,
                primary_rune,
                secondary_rune,
                winrate
            ) VALUES (
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