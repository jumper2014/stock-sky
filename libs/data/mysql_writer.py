#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 将指定的股票历史数据存入MySQL数据库

import tushare as ts
from sqlalchemy import create_engine, VARCHAR
from libs.db.mysqler import *
from libs.const.path import *



def save_his_to_mysql(stock_code, start=None):
    df = ts.get_hist_data(stock_code, start=start)
    engine = create_engine(STOCK_ENGINE_STR)
    # 存入数据库, 必须加dtype参数
    df.to_sql(history_data + stock_code, engine, if_exists='replace', dtype={'date': VARCHAR(10)})
    engine.dispose()
    print('done for {0}'.format(stock_code))


if __name__ == '__main__':
    stock_code = '000002'
    save_his_to_mysql(stock_code, start='2018-01-01')
