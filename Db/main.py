import os.path
import sqlite3
import sys
from pathlib import Path


sys.path.append(".")
from utils import DB_FILENAME


BASE_DIR = str(Path(__file__).parent.parent)
DB_PATH = os.path.join(BASE_DIR, DB_FILENAME)


class DbConn:

    def __init__(self):
        self.conn = sqlite3.connect(DB_PATH)
        self.cur = self.conn.cursor()

    def fetch_data(self, query: str, is_single_fetch=False):
        self.cur.execute(query)

        if is_single_fetch:
            return self.cur.fetchone(query)
        return self.cur.fetchall(query)

    def execute_and_commit_query(self, query: str):
        self.cur.execute(query)
        self.conn.commit()

    def close(self):
        self.conn.close()
