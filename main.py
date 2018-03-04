#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from sqlalchemy import create_engine, VARCHAR
import tushare as ts
from libs.date import now
from libs.db.mysqler import *

if __name__ == '__main__':
    # stock_code = '600846'
    stock_code = '000002'
    start = now()
    # df = ts.get_hist_data(stock_code, start='2018-02-26')
    df = ts.get_hist_data(stock_code, start='2010-01-01')
    print(df.index)
    # print(df['date'].dtypes)
    print(df['open'])

    # exit(0)
    # filename = 'hist_data_' + stock_code + '.csv'
    # if os.path.exists(filename):
    #     df.to_csv(filename, mode='a', header=None)
    # else:
    #     df.to_csv(filename)

    engine = create_engine(STOCK_ENGINE_STR)

    # 存入数据库, 必须加dtype参数
    df.to_sql('hist_data_'+stock_code, engine, if_exists='replace', dtype={'date': VARCHAR(10)})

    print("Time cost {0}".format(now() - start))
    # 追加数据到现有表
    # df.to_sql('hist_data',engine,if_exists='append')