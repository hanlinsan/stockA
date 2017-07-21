# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 16:17:16 2017

@author: Administrator
"""


import pandas as pd

frame = pd.read_csv('D:/StockListA/SH00.csv')
print(frame.columns)


with open('./SH.csv') as f :
    for line in f.readlines():
        print(line)


d = {'one':pd.Series([1,2,3]), 'two':pd.Series([4,5,6])}
print(d['one'])