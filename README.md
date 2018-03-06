# 股票天空
- 获取股票数据
- 存储到csv, MySQL数据库
- 根据历史数据筛选股票


### 安装和依赖
- MySQL数据库, 数据库名stock, 用户名密码为root/123456
- Python 2.7
- PipEnv(可选，建议安装，避免环境版本冲突和权限问题)
- tushare
- lxml, pandas, requests, bs4 (支持tushare, 建议从pipenv命令行安装)
- export PATH=$PATH:/usr/local/mysql/bin; pip install mysql-python
- configparser
- pyecharts, 它是一个用于生成 Echarts 图表的类库。Echarts 是百度开源的一个数据可视化 JS 库。主要用于数据可视化。
- 建议使用清华的源 pip install <pkg> -i https://pypi.tuna.tsinghua.edu.cn/simple



### 获取股票数据
- python libs/data/mysql_writer.py : 获取股票数据存储到MySQL
- python libs/data/csv_writer.py : 获取股票数据存储到MySQL
- python misc/tool/stock_code_spider/stock_code_spider.py: 抓取股票代码和名称，写入同目录data.csv
- python kline.py: 生成股票K线图

### 如何使用
- 抓取数据到MySQL: python main -t msql
- 抓取数据到CSV: python main -t csv
- 性能：500秒抓取3500只股票三年的数据


### 筛选股票
- TODO




### 开发计划
- todo: 展示均线
- todo: 从构建MongoDB数据结构
- todo: 读写MongoDB的库 
- todo: 构建测试程序
- -----------------
- done: 通过线程池批量下载历史数据
- done: 使用从tushare获得的股票代码代替从东方财富网获得股票代码
- done: 数据存储到csv
- done: 展示K线图
- done: 展示成交量图
- done: 股票代码和名称获取
- done: 日数据存储到MySQL
- done: Mac OS 安装MySQL
- done: Python 2.7环境
- done: PipEnv结合PyCharm
- done: 安装第三方库和依赖


### 感谢
- http://tushare.org/
- https://github.com/willowj/python_dataEE