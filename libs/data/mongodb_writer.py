#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 将指定的股票历史数据存入MongoDB数据库

import tushare as ts
from sqlalchemy import create_engine, VARCHAR
from libs.db.mysqler import *
from libs.const.path import *
import pymongo
import json


def save_his_to_mongodb(stock_code, conn=None, start=None):
    df = ts.get_hist_data(stock_code, start)
    conn.db.tickdata.insert(json.loads(df.to_json(orient='records')))
    print('done for {0}'.format(stock_code))


if __name__ == '__main__':
    stock_code = '000002'
    # save_his_to_mysql(stock_code, start='2018-01-01')
