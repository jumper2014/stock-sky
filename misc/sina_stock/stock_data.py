# -*-coding:utf-8 -*-
#
#

import requests
import time
import sys
import threading
from optparse import OptionParser

result_dict = dict()


def get_data(code):
    slice_num, value_num = 21, 3
    name, now = u'——无——', u'  ——无——'
    if code in ['s_sh000001', 's_sz399001']:
        slice_num = 23
        value_num = 1
    r = requests.get("http://hq.sinajs.cn/list=%s" % (code,))
    res = r.text.split(',')
    if len(res) > 1:
        name, now = r.text.split(',')[0][slice_num:], r.text.split(',')[value_num]
    result_dict[name] = now


def get_stock_data(codes):
    for code in codes:
        t = threading.Thread(target=get_data, args=(code,))
        t.setDaemon(True)
        t.start()
    main_thread = threading.currentThread()
    for t in threading.enumerate():
        if t is not main_thread:
            t.join()
    for key, value in result_dict.items():
        print key, value





if __name__ == '__main__':
    parser = OptionParser(description="Query the stock's value.", usage="%prog [-c] [-s]", version="%prog 1.0")
    parser.add_option('-c', '--stock-code', dest='codes',
                      help="the stock's code that you want to query.")
    parser.add_option('-s', '--sleep-time', dest='sleep_time', default=6, type="int",
                      help='How long does it take to check one more time.')
    options, args = parser.parse_args(args=sys.argv[1:])

    assert options.codes, "Please enter the stock code!"  # 是否输入股票代码
    if filter(lambda s: s[:-6] not in ('sh', 'sz', 's_sh', 's_sz'), options.codes.split(',')):  # 股票代码输入是否正确
        raise ValueError
    else:
        codes = options.codes.split(',')

    while True:
        get_stock_data(codes)
        print "---------"
        time.sleep(options.sleep_time)


