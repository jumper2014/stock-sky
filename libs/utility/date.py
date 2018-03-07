#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 日期相关函数

import time
import datetime


def date_before_today(days):
    """
    几天以前的日期
    :param days: 几天
    :return: 日期字符串，类似 "2018-03-06"
    """
    today = datetime.date.today()
    before = today - datetime.timedelta(days=days)
    return str(before)


def now():
    return time.time()


if __name__ == '__main__':
    print(str(date_before_today(1)))