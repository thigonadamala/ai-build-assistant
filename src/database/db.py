import os
import oracledb
from dotenv import load_dotenv

load_dotenv()


def get_required_env(name):
    value = os.getenv(name)

    if not value:
        raise RuntimeError(
            f"Variavel de ambiente obrigatoria nao configurada: {name}"
        )

    return value


def get_connection():
    return oracledb.connect(
        user=get_required_env("DB_USER"),
        password=get_required_env("DB_PASSWORD"),
        dsn=get_required_env("DB_DSN")
    )
