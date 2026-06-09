from src.database.db import get_connection


def create_table():
    connection = None
    cursor = None

    try:
        connection = get_connection()

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