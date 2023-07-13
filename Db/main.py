import sqlite3


class DbConn:

    def __init__(self):
        self.conn = sqlite3.connect("db.sqlite")
        self.cur = self.conn.cursor()

    def fetch_data(self, query: str, is_single_fetch=False):
        self.cur.execute(query)

        if is_single_fetch:
            return self.cur.fetchone(query)
        return self.cur.fetchall(query)

    def save_or_update_data(self, query: str):
        try:
            self.cur.execute(query)
        except Exception as e:
            

    def close_conn(self):
        self.conn.close()

    def get_or_create_db(self, query: str):
        if data:= not self.fetch_data(query, is_single_fetch=True):
            
