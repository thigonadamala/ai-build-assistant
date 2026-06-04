from src.db import get_connection

def load_lol(df):
    connection = None
    cursor = None

    try:
        # Abre conexão com Oracle usando a função centralizada em db.py
        connection = get_connection()
        cursor = connection.cursor()

        # SQL com bind variables para inserir builds de LoL
        sql = """
            INSERT INTO lol_builds (champion, role, item, winrate)
            VALUES (:1, :2, :3, :4)
        """

        # Converte o DataFrame em lista de tuplas, formato aceito pelo executemany
        dados = [tuple(linha) for linha in df.values]

        # Insere várias linhas de uma vez no banco
        cursor.executemany(sql, dados)

        # Confirma a transação no Oracle
        connection.commit()

        print("\nDados LoL inseridos com sucesso!")

    except Exception as e:
        # Exibe o erro caso a inserção falhe
        print("\nErro ao inserir dados LoL:")
        print(e)

    finally:
        # Fecha os recursos mesmo se ocorrer erro
        if cursor:
            cursor.close()

        if connection:
            connection.close()