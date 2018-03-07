#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 从数据库中读取每支股票最近两天的数据
# 判断5日，10日，30日均线的关系。

from pandas import DataFrame
from sqlalchemy import create_engine
from libs.db.stock_code import get_stock_codes, get_stocks
from libs.utility.date import now

col_ma5 = 8
col_ma10 = 9
col_ma20 = 10

DAY_5_10 = 'day_5_10'
DAY_10_20 = 'day_10_20'
STOCKS = get_stocks()


def is_golden_ma(engine, stock_code, period=DAY_5_10):
    df = get_stock_hist_from_mysql(engine, stock_code)
    if df is None:
        return
    # print(df)
    if df.shape[0] < 2:
        print("Error, {0} history data length less than 2".format(stock_code))
        return
    else:
        data1 = df.ix[0]
        data2 = df.ix[1]

        if period == DAY_5_10:
            fast_line = col_ma5
            slow_line = col_ma10
        elif period == DAY_10_20:
            fast_line = col_ma10
            slow_line = col_ma20
        else:
            # print("Error period")
            return
        # print('Latest:   {0} - {1}'.format(data1[fast_line], data1[slow_line]))
        # print('Previous: {0} - {1}'.format(data2[fast_line], data2 [slow_line]))

        if data1[fast_line] > data1[slow_line] and data2[fast_line] < data2[slow_line]:
            print('Find golden_ma: {0} - {1}'.format(stock_code, STOCKS[stock_code]))

            return True
        else:
            return False


def get_stock_hist_from_mysql(engine, stock_code):
    df = None
    try:
        result = engine.execute('select * from hist_data_{0} limit 2'.format(stock_code))
        ans = result.fetchall()
        df = DataFrame(ans)
    except Exception as e:
        print(e.message)

    return df


if __name__ == '__main__':
    start_time = now()
    engine = create_engine('mysql://root:123456@127.0.0.1:3306/stock')

    stocks = get_stock_codes()
    # stocks = ['603886']
    for stock in stocks:
        is_golden_ma(engine, stock)

    # 计时结束
    end_time = now()
    print('Time is: {0}'.format(end_time - start_time))
