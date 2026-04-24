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
            CREATE TABLE funcionarios (
                id NUMBER CONSTRAINT pk_funcionarios PRIMARY KEY,
                nome VARCHAR2(100) NOT NULL,
                idade NUMBER NOT NULL,
                cidade VARCHAR2(100) NOT NULL,
                salario NUMBER NOT NULL,
                setor VARCHAR2(100) NOT NULL
            )
        """)

        connection.commit()
        print("Tabela criada com sucesso!")

    except Exception as e:
        print("Erro ao criar a tabela:")
        print(e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    create_table()