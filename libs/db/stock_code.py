#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 获得所有的股票代码

from libs.utility.path import *


def get_stocks_info():
    stocks_info = list()
    with open(STOCK_CODE_FILE, mode='r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            name, code = line.split(',')
            stock = (code, name)
            stocks_info.append(stock)
            # print(code_info[0] + code_info[1])
    return stocks_info


def get_stocks():
    stocks = dict()
    with open(STOCK_CODE_FILE, mode='r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            name, code = line.split(',')
            stocks[str(code)] = name
            # print(code_info[0] + code_info[1])
    return stocks

def get_stock_codes():
    codes = list()
    with open(STOCK_CODE_FILE, mode='r') as f:
        lines = f.readlines()
        for line in lines:
            line = line.strip()
            name, code = line.split(',')
            codes.append(code)
    return codes


if __name__ == '__main__':
    get_stocks_info()
    print(get_stock_codes())