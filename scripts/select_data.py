import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

def select_data():
    connection = None
    cursor = None

    try:
        connection = oracledb.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dsn=os.getenv("DB_DSN")
        )

        cursor = connection.cursor()

        cursor.execute("SELECT * FROM funcionarios ORDER BY id")
        dados = cursor.fetchall()

        print("DADOS NA TABELA FUNCIONARIOS:")
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