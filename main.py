#!/usr/bin/env python
# coding=utf-8

import tushare


if __name__ == '__main__':
    import tushare as ts

    print(ts.get_hist_data('600848'))  # 一次性获取全部数据