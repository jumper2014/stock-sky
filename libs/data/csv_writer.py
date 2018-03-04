#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 将指定的股票历史数据存入csv文件

import tushare as ts
from libs.const.path import *


def save_his_to_csv(stock_code, start=None):
    df = ts.get_hist_data(stock_code, start=start)
    filename = stock_csv_path + '/' + history_data + stock_code + '.csv'
    if os.path.exists(filename):
        df.to_csv(filename, mode='w', header=None)
    else:
        df.to_csv(filename)
    print('done for {0}'.format(stock_code))


if __name__ == '__main__':
    stock_code = '000003'
    save_his_to_csv(stock_code)