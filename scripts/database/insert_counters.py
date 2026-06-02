import os
import oracledb
from dotenv import load_dotenv

load_dotenv()


def insert_counters():
    connection = None
    cursor = None

    counters = [
        ("Ahri", "Zed", "mid", 48.20),
        ("Ahri", "Fizz", "mid", 47.10),
        ("Ahri", "Kassadin", "mid", 46.50),
        ("Yasuo", "Malphite", "mid", 45.80),
        ("Yasuo", "Renekton", "mid", 46.30),
        ("Jinx", "Draven", "adc", 47.40),
    ]

    try:
        connection = oracledb.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dsn=os.getenv("DB_DSN")
        )

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