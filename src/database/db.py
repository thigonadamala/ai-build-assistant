import os
import oracledb
from dotenv import load_dotenv

load_dotenv()


def get_connection():
    wallet_path = os.getenv("DB_WALLET_PATH")
    wallet_password = os.getenv("DB_WALLET_PASSWORD")

    if wallet_path:
        return oracledb.connect(
            user=os.getenv("DB_USER"),
            password=os.getenv("DB_PASSWORD"),
            dsn=os.getenv("DB_DSN"),
            config_dir=wallet_path,
            wallet_location=wallet_path,
            wallet_password=wallet_password
        )

    return oracledb.connect(
        user=os.getenv("DB_USER"),
        password=os.getenv("DB_PASSWORD"),
        dsn=os.getenv("DB_DSN")
    )