from scipy.stats import kurtosis, skew
from adjustAndClean.StackData import StackData
from adjustAndClean.TAQCleaner import TAQCleaner
import numpy as np
import pandas as pd
import random
from numpy.linalg.linalg import _isEmpty2d

# Dataframe
baseDir = '/media/louis/DATA/Courant_dataset_matlab/R/'
startDate = '20070713'
endDate = '20070727'
        
# Suggested initial parameters, to calibrate
k_test = np.array([k * 5 for k in range(1,10)])
gamma_test = np.array([0.0005 * i * 5 for i in range(1,10)])
        
# Result arrays
skews = np.reshape([0. for i in range(0, 9*9)], (9,9))
kurtosiss = np.reshape([0. for i in range(0, 9*9)], (9,9))
        
print(skews, kurtosiss)
        
# S&P500 tickers
s_p500 = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/s_p500.xlsx'
s_p500xls = pd.read_excel(open(s_p500,'rb'), sheet_name='WRDS')
s_ptickers = np.unique((np.array(s_p500xls['Ticker Symbol'])).astype(str))
s_ptickers = s_ptickers[:-1]
        
# Stack data, by ticker
subtickers = [random.randint(1,300) for i in range(0,10)]
l = len(subtickers)
print(subtickers)
sampleticks = s_ptickers[subtickers]
print(sampleticks)
stacks = np.array([StackData(baseDir, startDate, endDate, ticker) for ticker in sampleticks])
print(stacks)
for s in stacks:
    print('hey')
    s.addTrades()

i = 0
for k in k_test:
    j = 0
    for gamma in gamma_test:
        for s in stacks:
            trades = s.getStackedTrades()
            if (trades.size == 0):
                continue
            cleaner = TAQCleaner([], trades, k, gamma)
            trades = np.delete(trades, cleaner.cleanTradesIndices(), axis = 0)
            skews[i,j] += skew(np.array(trades[:,-2].astype(np.float)))
            kurtosiss[i,j] += kurtosis(np.array(trades[:,-2].astype(np.float)))
        skews[i,j] = skews[i,j] / l
        kurtosiss[i,j] = kurtosiss[i,j] / l
        j += 1
        print(i,j)
    i += 1

min1 = np.unravel_index(np.argmin(skews, axis=None), skews.shape)
min2 = np.unravel_index(np.argmin(kurtosiss, axis=None), kurtosiss.shape)

print(min1)
print(min2)

print(skews)
print(kurtosiss)

