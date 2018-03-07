#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 移动平均线选股


import tushare as ts
from libs.utility.date import date_before_today


DAY_5_10 = 'day_5_10'
DAY_10_20 = 'day_10_20'


def is_golden_ma(stock_code, period=DAY_5_10):
    df = get_stock_hist(stock_code, 10)
    if df.shape[0] < 2:
        print("Error, history data length less than 2")
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
            print("Error period")
            return

        if data1[fast_line] > data1[slow_line] and data2[fast_line] < data2[slow_line]:
            print('Find golden_ma: {0}'.format(stock_code))
            print('Latest:   {0} - {1}'.format(data1[fast_line], data1[slow_line]))
            print('Previous: {0} - {1}'.format(data2[fast_line], data2 [slow_line]))
            return True
        else:
            return False


def get_stock_hist(stock_code, days):
    start = date_before_today(days)
    df = ts.get_hist_data(stock_code, start)
    return df


if __name__ == '__main__':
    is_golden_ma('300477')