from src.database.db import get_connection


def test_connection():
    connection = None

    try:
        connection = get_connection()

        print("Conexão com Oracle realizada com sucesso!")

    except Exception as e:
        print("Erro ao conectar no Oracle:")
        print(e)

    finally:
        if connection:
            connection.close()


if __name__ == "__main__":
    test_connection()