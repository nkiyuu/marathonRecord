import sqlite3
from sqlalchemy import *
import sqlalchemy.sql
import sqlalchemy.orm
import sqlalchemy.ext.declarative
import config
Base = sqlalchemy.ext.declarative.declarative_base()
url = 'sqlite:///' + config.DB_PATH
engine = sqlalchemy.create_engine(url)
Session = sqlalchemy.orm.sessionmaker(bind=engine)


class User(Base):
    '''
    usersテーブルのカラム
    '''
    __tablename__ = 'users'
    id = Column(Integer, primary_key=True)
    name = Column(Text, unique=True, nullable=False)
    created_at = Column(Date, server_default=sqlalchemy.sql.func.now(), nullable=False)
    delete_at = Column(sqlalchemy.Text, default=None)


class Record(Base):
    '''
    recordsテーブルのカラム
    '''
    __tablename__ = 'records'
    id = Column(Integer, primary_key=True)
    user_id = Column(Integer, nullable=False)
    course_id = Column(Integer, nullable=False)
    time = Column(Text, nullable=False)
    date = Column(Date, server_default=sqlalchemy.sql.func.now(), nullable=False)
    create_at = Column(Date, server_default=sqlalchemy.sql.func.now())
    delete_at = Column(Date)


class Course(Base):
    '''
    coursesテーブルのカラム
    '''
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    url = Column(Text, nullable=False)
    distance = Column(REAL, nullable=False)
    create_at = Column(Date, server_default=sqlalchemy.sql.func.now())
    delete_at = Column(Date)


def create_tables():
    '''
    テーブルデータの作成
    '''
    Base.metadata.create_all(engine)
