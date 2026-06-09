from src.database.db import get_connection


def create_runes_table():
    connection = None
    cursor = None

    try:
        connection = get_connection()

        cursor = connection.cursor()

        cursor.execute("""
            CREATE TABLE lol_runes (
                id NUMBER GENERATED ALWAYS AS IDENTITY
                CONSTRAINT pk_lol_runes PRIMARY KEY,

                champion VARCHAR2(50) NOT NULL,
                role VARCHAR2(20) NOT NULL,
                primary_rune VARCHAR2(100) NOT NULL,
                secondary_rune VARCHAR2(100) NOT NULL,
                winrate NUMBER(5,2) NOT NULL
            )
        """)

        connection.commit()

        print("Tabela lol_runes criada com sucesso!")

    except Exception as e:
        print("Erro ao criar a tabela lol_runes:")
        print(e)

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


if __name__ == "__main__":
    create_runes_table()