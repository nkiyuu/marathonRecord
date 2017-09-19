import sqlite3
import sqlalchemy
import sqlalchemy.sql
import sqlalchemy.orm
import sqlalchemy.ext.declarative
from sqlalchemy.dialects.sqlite import DATE
import datetime

from config import DB_PATH

Base = sqlalchemy.ext.declarative.declarative_base()
url = 'sqlite:///' + DB_PATH
engine = sqlalchemy.create_engine(url, echo=True)
Session = sqlalchemy.orm.sessionmaker(bind=engine)


class UserModel(Base):
    '''
    usersテーブルのカラム
    '''
    __tablename__ = 'users'
    id = sqlalchemy.Column(sqlalchemy.Integer, primary_key=True)
    name = sqlalchemy.Column(sqlalchemy.Text, unique=True, nullable=False)
    created_at = sqlalchemy.Column(sqlalchemy.Date, server_default=sqlalchemy.sql.func.now(), nullable=False)
    delete_at = sqlalchemy.Column(sqlalchemy.Text, default=None)


def create_tables():
    '''
    テーブルデータの作成
    :return:
    '''
    Base.metadata.create_all(engine)
