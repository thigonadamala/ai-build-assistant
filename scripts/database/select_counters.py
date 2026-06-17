from src.database.db import get_connection


def select_data():
    connection = None
    cursor = None

    try:
        connection = get_connection()
        cursor = connection.cursor()

        cursor.execute("""
            SELECT *
            FROM lol_counters
            ORDER BY champion
        """)

        dados = cursor.fetchall()

        print("DADOS NA TABELA LOL_COUNTERS:")

        for linha in dados:
            print(linha)

    except Exception as e:
        print("Erro ao consultar a tabela:")
        print(e)

    finally:
        if cursor:
            cursor.close()

        if connection:
            connection.close()


if __name__ == "__main__":
    select_data()
