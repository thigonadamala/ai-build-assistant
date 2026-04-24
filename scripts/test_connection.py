import os
import oracledb
from dotenv import load_dotenv

load_dotenv()

def test_connection():
    try:
        connection = oracledb.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dsn=os.getenv("DB_DSN")
        )

        print("Conexão com Oracle realizada com sucesso!")

        connection.close()

    except Exception as e:
        print("Erro ao conectar no Oracle:")
        print(e)

if __name__ == "__main__":
    test_connection()