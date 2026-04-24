import os
import oracledb
from dotenv import load_dotenv

# Carrega variáveis do arquivo .env para dentro do ambiente
load_dotenv()

def get_connection():
    # Cria e retorna uma conexão com o Oracle
    # Centralizar isso aqui evita duplicação de código em outros arquivos
    return oracledb.connect(
        user=os.getenv("DB_USER"),        # Usuário do banco vindo do .env
        password=os.getenv("DB_PASSWORD"),# Senha do banco vindo do .env
        dsn=os.getenv("DB_DSN")           # String de conexão (host/porta/service)
    )