#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
"""
date：日期
open：开盘价
high：最高价
close：收盘价
low：最低价
volume：成交量
price_change：价格变动
p_change：涨跌幅
ma5：5日均价
ma10：10日均价
ma20: 20日均价
v_ma5:5日均量
v_ma10:10日均量
v_ma20:20日均量
turnover:换手率[注：指数无此项]
"""


class StockDay(object):
    """
    描述每日股票数据的类
    """
    def __init__(self, code, date, open, high, close, low, volume, price_change, p_change,
                 ma5, ma10, ma20, v_ma5, v_ma10, v_ma20, turnover):
        self.code = code
        self.date = date
        self.open = open
        self.high = high
        self.close = close
        self.low = low
        self.volume = volume
        self.price_change = price_change
        self.p_change = p_change
        self.ma5 = ma5
        self.ma10 = ma10
        self.ma20 = ma20
        self.v_ma5 = v_ma5
        self.v_ma10 = v_ma10
        self.v_ma20 = v_ma20
        self.turnover = turnover

    def is_yang(self):
        """
        收盘价高于开盘价，阳线，反之，阴线
        :return:
        """
        return self.close > self.open

    def is_rise(self):
        """
        判断是否上涨
        :return:
        """
        return self.price_change > 0


if __name__ == '__main__':
    pass