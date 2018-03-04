#!/usr/bin/env python
# coding=utf-8

from libs.ui.kline_candle import kline_js
import tushare as ts

if __name__ == '__main__':

    df = ts.get_hist_data('hs300', ktype='5')
    kline_js('hs300_k-line-5min',
             df,
             ma=('ma10', 'ma20'),
             width=800, height=400, render_path='./misc/html/k-line.html'
             )