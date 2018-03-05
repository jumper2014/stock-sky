#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian

import optparse
import threadpool
from libs.date import now
from libs.data.mysql_writer import save_his_to_mysql
from libs.data.csv_writer import save_his_to_csv
from libs.db.stock_code import get_stock_codes
from sqlalchemy import create_engine, VARCHAR
from libs.db.mysqler import *
from libs.const.path import *

if __name__ == '__main__':
    start_time = now()

    stocks = get_stock_codes()
    # stocks = ['000001', '000002']

    parser = optparse.OptionParser(
        usage="%prog [optons] [<arg1> <arg2> ...]",
        version="1.0"
    )
    parser.add_option('-t', '--target', dest='target', type='string', default='csv', help='csv/mysql')
    parser.add_option('-s', '--start', dest='start', type='string', default=None, help='start date')

    (options, args) = parser.parse_args()
    target = options.target
    start_date = options.start

    if target == 'csv':
        target_func = save_his_to_csv
    elif target == 'mysql':
        target_func = save_his_to_mysql
    else:
        print('wrong target!')
        exit(0)

    args = list()
    engine = create_engine(STOCK_ENGINE_STR)
    engines = [engine for i in range(len(stocks))]
    starts = [start_date for i in range(len(stocks))]
    nones = [None for i in range(len(stocks))]
    if start_date is not None:
        args = zip(zip(stocks, engines, starts), nones)
        # args = zip(stocks, [start_date for i in range(len(stocks))])
    else:
        args = zip(zip(stocks, engines), nones)
        print(args)

    # 针对每个板块写一个文件,启动一个线程来操作
    # 使用线程池来做
    pool_size = 10
    pool = threadpool.ThreadPool(pool_size)
    requests = threadpool.makeRequests(target_func, args)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    # 完成后退出
    pool.dismissWorkers(pool_size, do_join=True)

    # 计时结束
    end_time = now()
    print('Total save {0} stocks'.format(len(stocks)))
    print('Time is: {0}'.format(end_time - start_time))
