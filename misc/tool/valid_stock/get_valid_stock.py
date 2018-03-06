#!/usr/bin/env python
# coding=utf-8
# author: zengyuetian
# 获取可以通过tushare获得数据的股票信息
# 直接通过tushare提供的股票列表来获取，比抓取东方财富网的更可靠

import tushare as ts

if __name__ == '__main__':
    df = ts.get_stock_basics()
    names = list(df['name'])
    codes = list(df.index)
    # codes = map(int, codes)
    stocks = dict(zip(names, codes))

    lines = list()
    sorted_stocks = sorted(stocks.iteritems(), key=lambda d: int(d[1]), reverse=False)
    for name, code in sorted_stocks:
        print(name + "->" + code)
        lines.append(name + "," + code + '\n')
    print("Total stock num: {0}".format(len(sorted_stocks)))

    # 写入csv文件，为了速度，直接通过文件形式写入，如果使用csv库，性能会大幅下降
    with open('data.csv', 'w') as f:
        f.writelines(lines)
    code_and_names = ['{0},{1}\n'.format(codes[i], names[i]) for i in range(len(codes))]
