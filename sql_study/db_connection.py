from getpass import getpass
from pathlib import Path

from IPython import get_ipython
from sqlalchemy import URL, create_engine
from sqlalchemy.engine import Engine


def connect_sakila() -> Engine:
    """ローカルMySQLのsakilaデータベースに接続する。"""

    password = getpass("MySQLのパスワード：")

    url = URL.create(
        "mysql+pymysql",
        username="root",
        password=password,
        host="127.0.0.1",
        port=3306,
        database="sakila",
        query={"charset": "utf8mb4"},
    )

    return create_engine(
        url,
        pool_pre_ping=True,
    )


def setup_sakila(displaylimit: int | None = 5) -> Engine:
    """JupyterでsakilaデータベースとJupySQLの実行環境を設定する。"""

    ip = get_ipython()

    if ip is None:
        raise RuntimeError(
            "この関数はJupyter Notebook上で実行してください。"
        )

    # JupySQLがまだ読み込まれていない場合のみ読み込む
    if ip.find_cell_magic("sql") is None:
        ip.run_line_magic("load_ext", "sql")

    # connect_sakila()を使用してMySQLに接続する
    engine = connect_sakila()

    # 「%sql engine」で使用できるように、
    # Jupyter Notebookの変数として登録する
    ip.user_ns["engine"] = engine
    ip.run_line_magic("sql", "engine")

    # SQLの実行結果として表示する最大行数を設定する
    if displaylimit is None:
        ip.run_line_magic(
            "config",
            "SqlMagic.displaylimit = None",
        )
    else:
        ip.run_line_magic(
            "config",
            f"SqlMagic.displaylimit = {displaylimit}",
        )

    # SQL実行時の補足メッセージを最小限にする
    ip.run_line_magic(
        "config",
        "SqlMagic.feedback = 0",
    )

    # データベースの接続情報を表示しない
    ip.run_line_magic(
        "config",
        "SqlMagic.displaycon = False",
    )

    return engine


def save_result_csv(result, filename: str) -> Path:
    """SQLの実行結果をCSVファイルとして保存する。"""

    # db_connection.pyと同じ場所にresultsフォルダーを作成する
    output_dir = Path(__file__).resolve().parent / "results"
    output_dir.mkdir(
        parents=True,
        exist_ok=True,
    )

    # CSVファイルの保存先を設定する
    file_path = output_dir / filename

    # SQLの実行結果をCSVファイルとして保存する
    result.DataFrame().to_csv(
        file_path,
        index=False,
        encoding="utf-8-sig",
    )

    print(f"保存完了：{file_path}")

    return file_path