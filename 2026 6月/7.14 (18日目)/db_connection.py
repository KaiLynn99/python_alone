from getpass import getpass

from sqlalchemy import URL, create_engine
from sqlalchemy.engine import Engine


def connect_sakila() -> Engine:
    """ローカルのMySQLのsakilaデータベースに接続する。"""
    password = getpass("MySQL パスワード: ")

    url = URL.create(
        "mysql+pymysql",
        username="root",
        password=password,
        host="127.0.0.1",
        port=3306,
        database="sakila",
        query={"charset": "utf8mb4"},
    )

    return create_engine(url, pool_pre_ping=True)