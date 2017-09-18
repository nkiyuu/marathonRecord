import re
import datetime as dt
import sqlite3

from config import DB_PATH


class Parent():
    def __init__(self):
        '''
        初期設定をしてdbに接続する
        '''
        self.closed = False
        self.db_path = DB_PATH

        self.connection = sqlite3.connect(
            self.db_path,
            detect_types=sqlite3.PARSE_DECLTYPES | sqlite3.PARSE_COLNAMES
        )
        self.cursor = self.connection.cursor()

    def __del__(self):
        return self.close()

    def __enter__(self):
        return self

    def close(self):
        if self.closed:
            return
        self.closed = True
        self.connection.close()
