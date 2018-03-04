#!/usr/bin/env python
# coding=utf-8
# MySQL操作库

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

MYSQL_USER = 'root'
MYSQL_PASSWORD = '123456'
MYSQL_IP = '127.0.0.1'
MYSQL_DB = 'mysql'
STOCK_DB = 'stock'
MYSQL_ENGINE_STR = 'mysql://{0}:{1}@{2}/{3}?charset=utf8'.format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_IP, MYSQL_DB)
STOCK_ENGINE_STR = 'mysql://{0}:{1}@{2}/{3}?charset=utf8'.format(MYSQL_USER, MYSQL_PASSWORD, MYSQL_IP, STOCK_DB)


def reset_db(db_name):
    create_db(db_name)


def drop_db(db_name):
    engine = create_engine(MYSQL_ENGINE_STR)
    db_session = sessionmaker(bind=engine, autocommit=True)
    session = db_session()
    session.execute('drop database if exists {0} ;'.format(db_name))
    print('drop db done')


def create_db(db_name):
    engine = create_engine(MYSQL_ENGINE_STR)
    db_session = sessionmaker(bind=engine, autocommit=True)
    session = db_session()
    session.execute('drop database if exists {0} ;'.format(db_name))
    session.execute('create database {0};'.format(db_name))
    print('create db done')


if __name__ == '__main__':
    create_db('stock')