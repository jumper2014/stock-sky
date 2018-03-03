#!/usr/bin/env python
# coding=utf-8

# import pymysql
# pymysql.install_as_MySQLdb()
from sqlalchemy import create_engine
import tushare as ts
from libs.date import now


if __name__ == '__main__':
    stock_code = '600846'
    start = now()
    df = ts.get_hist_data(stock_code)
    engine = create_engine('mysql://root:123456@127.0.0.1/stocksky?charset=utf8')

    # 存入数据库
    df.to_sql(stock_code + '_hist_data', engine, if_exists='replace')

    print("Time cost {0}".format(now() - start))
    # 追加数据到现有表
    # df.to_sql('hist_data',engine,if_exists='append')