# -*- coding: utf-8 -*-
"""
Created on Wed Jul  5 15:09:06 2017

@author: hanlinsan
"""
import os
import requests
from bs4 import BeautifulSoup
from datetime import date
import pandas as pd

#采集数据时的日期
currentDate = date.today()

#雪球网站采集信息的BaseUrl
XUEQIU_URL = "https://xueqiu.com/S/"
#反爬虫信息头设置
HEADERS = {'user-agent':'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/58.0.3029.81 Safari/537.36'}

#取得沪市股票代码列表
stocksCodeFrame = pd.read_csv('D:/StockListA/SH00.csv')['A股代码']

#根据传入的市场类型返回要抓取的URL
#沪市：SH
#深市：SZ

def getStockUrl(market, stockCode):
    return XUEQIU_URL + market + stockCode



def gatherStockInfo(url, code):
    stockCode = code
    print(code)
    r = requests.get(stockUrl, headers=HEADERS)
    soup = BeautifulSoup(r.text, 'lxml')
    stockTable = soup.select('.topTable')
    # 交易时间时是当前的股票即时价格，收市后是收盘价格
    currentStockPrice = soup.find("div", class_='currentInfo').strong.string[1:]
    # print(stockTable)
    # <table class="topTable">
    #
    # <tr>
    # <td>今开：<span>16.93</span></td>
    # <td>最高：<span id="quote-high">17.23</span></td>
    # <td>52周最高：<span>18.29</span></td>
    # <td title="当日成交量，单位：股">成交量：<span id="quote-volume">7046.73万股</span></td>
    # </tr>
    #
    # <tr class="seperateTop">
    # <td>昨收：<span>16.95</span></td>
    # <td>最低：<span id="quote-low">16.91</span></td>
    # <td>52周最低：<span>15.25</span></td>
    # <td>成交额：<span>12.04亿</span></td>
    # </tr>
    #
    # <tr class="seperateBottom">
    # <td>涨停价：<span>18.65</span></td>
    # <td>总市值：<span>2064.72亿</span></td>
    # <td title="最近报告期每股收益，单位：人民币">每股收益：<span>0.19</span></td>
    # <td>市盈率(静)/(动)：<span>19.92/18.73</span></td>
    # </tr>
    #
    # <tr>
    # <td>跌停价：<span>15.26</span></td>
    # <td>总股本：<span>121.17亿</span></td>
    # <td title="最近报告期每股净资产，单位：人民币">每股净资产：<span>12.02</span></td>
    # <td>市净率(动)：<span>1.42</span></td>
    # </tr>
    #
    # <tr>
    # <td title="单位：%">振幅：<span>1.89%</span></td>
    # <td>流通股本：<span>98.15亿</span></td>
    # <td>每股股息：<span>0.50</span></td>
    # <td>市销率(动)：<span>5.26</span></td>
    # </tr>
    #
    #
    # </table>
    #
    trs = stockTable[0].find_all('tr')
    # specific stock datum gathered from xueqiu
    stockDatas = {'当天价格': currentStockPrice}
    line = [currentStockPrice]
    indexs = ['当天价格']
    for tr in trs:
        for td in tr.find_all('td'):
            name, value = td.strings
            line.append(value)
            indexs.append(name)
            stockDatas[name] = value
    codeFile = 'd:/StockListA/' + stockCode + '.csv'
    print(codeFile)
    # mode = 'at' if os.path.exists(codeFile) else 'xt'
    #
    # with open(codeFile, mode) as f :
    #    f.write(','.join(line))
    if not os.path.exists(codeFile):
        with open(codeFile, 'xt') as f:
            f.write(','.join(indexs) + '\n')
            f.write(','.join(line) + '\n')
    else:
        with open(codeFile, 'at') as f:
            f.write(','.join(line) + '\n')



#迭代返回抓取的数据
for code in stocksCodeFrame:
    stockUrl = getStockUrl('SH', str(code))
    try:
        gatherStockInfo(stockUrl, str(code))
    except Exception:
        print(str(code))
        continue


