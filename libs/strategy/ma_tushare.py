#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 从tushare接口读取每支股票最近一段时间的数据
# 判断5日，10日，30日均线的关系。


import tushare as ts
import threadpool
from libs.utility.date import date_before_today
from libs.utility.date import now
from libs.db.stock_code import get_stock_codes, get_stocks


DAY_5_10 = 'day_5_10'
DAY_10_20 = 'day_10_20'
STOCKS = get_stocks()


def is_golden_ma(stock_code, period=DAY_5_10):
    df = get_stock_hist(stock_code, 10)
    if df.shape[0] < 2:
        # print("Error, {0} history data length less than 2".format(stock_code))
        return
    else:
        data1 = df.ix[0]
        data2 = df.ix[1]

        if period == DAY_5_10:
            fast_line = 'ma5'
            slow_line = 'ma10'
        elif period == DAY_10_20:
            fast_line = 'ma10'
            slow_line = 'ma20'
        else:
            # print("Error period")
            return

        if data1[fast_line] > data1[slow_line] and data2[fast_line] < data2[slow_line]:
            print('Find golden_ma: {0} - {1}'.format(stock_code, STOCKS[stock_code]))
            # print('Latest:   {0} - {1}'.format(data1[fast_line], data1[slow_line]))
            # print('Previous: {0} - {1}'.format(data2[fast_line], data2 [slow_line]))
            return True
        else:
            return False


def get_stock_hist(stock_code, days):
    start = date_before_today(days)
    df = ts.get_hist_data(stock_code, start)
    return df


if __name__ == '__main__':

    start_time = now()

    stocks = get_stock_codes()

    pool_size = 10
    pool = threadpool.ThreadPool(pool_size)
    requests = threadpool.makeRequests(is_golden_ma, stocks)
    [pool.putRequest(req) for req in requests]
    pool.wait()
    # 完成后退出
    pool.dismissWorkers(pool_size, do_join=True)

    # 计时结束
    end_time = now()
    print('Total save {0} stocks'.format(len(stocks)))
    print('Time is: {0}'.format(end_time - start_time))