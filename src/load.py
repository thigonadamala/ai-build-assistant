from src.db import get_connection

def load_funcionarios(df):
    connection = None
    cursor = None

    try:
        # Abre conexão com o banco usando função centralizada
        connection = get_connection()
        cursor = connection.cursor()

        # SQL com bind variables
        # Evita SQL injection e melhora performance no Oracle
        sql = """
            INSERT INTO funcionarios (id, nome, idade, cidade, salario, setor)
            VALUES (:1, :2, :3, :4, :5, :6)
        """

        # Converte o DataFrame em lista de tuplas
        # Formato exigido pelo executemany
        dados = [tuple(linha) for linha in df.values]

        # Insere vários registros de uma vez (mais eficiente que loop)
        cursor.executemany(sql, dados)

        # Confirma a transação no banco
        connection.commit()

        print("\nDados inseridos com sucesso no Oracle!")

    except Exception as e:
        # Captura qualquer erro durante a inserção
        print("\nErro ao inserir dados no Oracle:")
        print(e)

    finally:
        # Garante que recursos sejam liberados mesmo com erro
        if cursor:
            cursor.close()

        if connection:
            connection.close()