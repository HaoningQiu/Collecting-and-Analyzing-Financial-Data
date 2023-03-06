# -*- coding: utf-8 -*-
"""
Created on Mon Nov 22 11:55:49 2021

@author: Edward
"""

import sys
import pandas as pd
import numpy as np
import statsmodels.api as sm
import matplotlib.pyplot as plt
from scipy import stats

data = pd.read_csv('preqin-lbo-data-1.csv')
data['leverage'] = 100 * data['debt'] / data['size']
data['profit'] = 100 * data['ebitda'] / data['revenue']
data = data[data['leverage'] <= 100]
nBins = 30
data['bin'] = pd.qcut(data['profit'], nBins, labels = False) + 1
dataBinned = data.groupby('bin')['profit', 'leverage'].mean()
x = dataBinned['profit']
y = dataBinned['leverage']
slope,intercept,r_value,p_value,std_err = stats.linregress(x,y)
line = slope * x + intercept
fig = plt.figure()
plt.plot(dataBinned['profit'], dataBinned['leverage'], 'o',dataBinned['profit'], line)
plt.xlabel("Target Company's Profit Margin (%)")
plt.ylabel("Fund's Leverage (%)")
fig.savefig("leverage-profit-binned-fit.png")
