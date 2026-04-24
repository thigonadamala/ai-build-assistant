import os
import pandas as pd
import oracledb
from dotenv import load_dotenv

load_dotenv()

def extract():
    df = pd.read_csv("data/funcionarios.csv")
    print("DADOS BRUTOS:")
    print(df)
    return df

def transform(df):
    df = df.dropna()
    df = df.reset_index(drop=True)

    print("\nDADOS TRATADOS:")
    print(df)
    return df

def load(df):
    connection = None
    cursor = None

    try:
        connection = oracledb.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dsn=os.getenv("DB_DSN")
        )

        cursor = connection.cursor()

        sql = """
            INSERT INTO funcionarios (id, nome, idade, cidade, salario, setor)
            VALUES (:1, :2, :3, :4, :5, :6)
        """

        dados = [tuple(linha) for linha in df.values]

        cursor.executemany(sql, dados)
        connection.commit()

        print("\nDados inseridos com sucesso no Oracle!")

    except Exception as e:
        print("\nErro ao inserir dados no Oracle:")
        print(e)

    finally:
        if cursor:
            cursor.close()
        if connection:
            connection.close()

if __name__ == "__main__":
    df = extract()
    df = transform(df)
    load(df)