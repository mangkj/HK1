from impactModel.FileManager import FileManager
import numpy as np
import pandas as pd
from adjustAndClean.TAQAdjust import TAQAdjust
from adjustAndClean.TAQCleaner import TAQCleaner
from adjustAndClean.StackData import StackData

class HowToLoop(object):
    '''
    For you Canel and Michael: How to loop & use StackData, TAQAdjust and TAQCleaner
    '''

    def __init__(self, baseDir, startDate, endDate ):
        '''
        '''
        ticker = 'IBM'
        
        # FIRST: Take S&P500 tickers
        s_p500 = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/s_p500.xlsx'
        s_p500xls = pd.read_excel(open(s_p500,'rb'), sheet_name='WRDS')
        s_ptickers = np.unique((np.array(s_p500xls['Ticker Symbol'])).astype(str))
        s_ptickers = s_ptickers[:-1]
       

        # THEN: Loop through tickers and stack them separately
        for ticker in s_ptickers:
            
            # Stack everything
            stack = StackData(baseDir, startDate, endDate, ticker)
            stack.addTrades()
            stack.addQuotes()
            
            # Get results
            quotes = stack.getStackedQuotes()
            trades = stack.getStackedTrades()
            
            # Adjust
            adjuster = TAQAdjust( quotes, trades, ticker, s_p500 )
            adjuster.adjustQuote()
            adjuster.adjustTrade()
            
            # Clean
            cleaner = TAQCleaner(quotes, trades, k=5, gamma = 0.005)
            quotes = np.delete(quotes, cleaner.cleanQuotesIndices(), axis = 0)
            trades = np.delete(trades, cleaner.cleanTradesIndices(), axis = 0)
            
        """ The datastructure to store those elements is up to you """
