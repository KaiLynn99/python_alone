from getpass import getpass

from sqlalchemy import URL, create_engine
from sqlalchemy.engine import Engine


def connect_sakila() -> Engine:
    """로컬 MySQL의 sakila 데이터베이스에 연결한다."""
    password = getpass("MySQL 비밀번호: ")

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