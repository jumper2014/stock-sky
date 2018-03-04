#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

from libs.date import now
from libs.data.mysql_writer import *
from libs.data.csv_writer import *

if __name__ == '__main__':
    # stock_code = '600846'
    stock_code = '000002'
    start = now()
    # df = ts.get_hist_data(stock_code, start='2018-02-26')
    save_his_to_csv(stock_code, start='2010-01-01')
    print("Time cost {0}".format(now() - start))
