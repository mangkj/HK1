from scipy.stats import kurtosis, skew
from adjustAndClean.StackData import StackData
from adjustAndClean.TAQCleaner import TAQCleaner
import numpy as np
import pandas as pd

""" This program allows us to calibrate k and gamma parameters.
    We loop through a sample of stocks between a certain timeframe,
    we stack them and we try to clean the data with several values of
    k and gamma"""

# Dataframe
baseDir = '/media/louis/DATA/Courant_dataset_matlab/R/'
startDate = '20070713'
endDate = '20070727'
        
# Suggested initial parameters, to calibrate
k_test = np.array([k for k in range(1,16)])
gamma_test = np.array([0.0005 * i for i in range(1,16)])
        
# Result arrays
skews = np.reshape([0 for i in range(0, 15*15)], (15,15))
kurtosis = np.reshape([0 for i in range(0, 15*15)], (15,15))
        
print(skews, kurtosis)
        
# S&P500 tickers
s_p500 = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/s_p500.xlsx'
s_p500xls = pd.read_excel(open(s_p500,'rb'), sheet_name='WRDS')
s_ptickers = np.unique((np.array(s_p500xls['Ticker Symbol'])).astype(str))
s_ptickers = s_ptickers[:-1]
        
# Stack data, by ticker
sampleticks = s_ptickers[0:1]
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
            print(i,j)
            trades = s.getStackedTrades()
            cleaner = TAQCleaner([], trades, k, gamma)
            trades = np.delete(trades, cleaner.cleanTradesIndices(), axis = 0)
            skews[i][j] += skew(np.array(trades[:,-2].astype(np.float)))
        j += 1
    i += 1

min = np.unravel_index(np.argmin(skews, axis=None), skews.shape)

print(min)


