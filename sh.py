# -*- coding: utf-8 -*-
"""
Created on Thu Jul 20 16:17:16 2017

@author: Administrator
"""


import pandas as pd

frame = pd.read_csv('./SH0.csv')
print(frame.columns)


#with open('./SH.csv') as f :
#    for line in f.readlines():
#        print(line)