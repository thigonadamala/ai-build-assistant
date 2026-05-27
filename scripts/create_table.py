import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

def create_table():
    connection = None
    cursor = None

    try:
        connection = oracledb.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dsn=os.getenv("DB_DSN")
        )

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE lol_counters (
                id NUMBER GENERATED ALWAYS AS IDENTITY
                CONSTRAINT pk_lol_counters PRIMARY KEY,

                champion VARCHAR2(50) NOT NULL,
                counter_champion VARCHAR2(50) NOT NULL,
                role VARCHAR2(20) NOT NULL,
                winrate NUMBER(5,2) NOT NULL
            )
        """)

        connection.commit()
        print("Tabela lol_counters criada com sucesso!")

    except Exception as e:
        print("Erro ao criar a tabela lol_counters:")
        print(e)

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()

if __name__ == "__main__":
    create_table()