#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 获得所有的股票代码

from libs.utility.path import MISC_PATH


def get_stocks_info():
    stock_code_csv = MISC_PATH + '/tool/stock_code_spider/data.csv'
    stocks_info = list()
    with open(stock_code_csv, mode='r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            name, code = line.split(',')
            stock = (code, name)
            stocks_info.append(stock)
            # print(code_info[0] + code_info[1])
    return stocks_info


def get_stock_codes():
    stock_code_csv = MISC_PATH + '/tool/stock_code_spider/data.csv'
    codes = list()
    with open(stock_code_csv, mode='r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            name, code = line.split(',')
            codes.append(code)
    return codes


if __name__ == '__main__':
    get_stocks_info()
    print(get_stock_codes())