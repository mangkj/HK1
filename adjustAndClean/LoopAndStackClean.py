from impactModel.FileManager import FileManager
from adjustAndClean.TAQCleaner import TAQCleaner
import numpy as np

class LoopAndStackClean(object):
    '''
    '''
    
    def __init__(self, baseDir, startDate, endDate, ticker):
        '''
        '''
        self._fm = FileManager( baseDir )
        
        # Retrieve list of trading days for trades & quotes files
        self._datesT = self._fm.getTradeDates(startDate, endDate) # 20070620, 20070621, ...
        self._datesQ = self._fm.getQuoteDates(startDate, endDate)
        
        # Stacked data
        self._stackedQuotes = np.empty((0,6))
        self._stackedTrades = np.empty((0,4))
        
        # Ticker searched
        self._ticker = ticker

    # Quotes
    def addCleanedQuotes(self):
        for date in self._datesQ:
            quoteFile = self._fm.getQuotesFile(date, self._ticker)
            tradeFile = self._fm.getTradesFile(date, self._ticker)
            cleaner = TAQCleaner( quoteFile, tradeFile)
            cleaner.cleanQuotes()
            
            # Append the day data [TICKER, TIMESTAMP, BIDPRICE, BIDSIZE, ASKPRICE, ASKSIZE]
            length = quoteFile.getN()
            for i in range(0, length):
                newRow = np.array([[self._ticker, quoteFile.getTimestamp(i), quoteFile.getBidPrice(i), quoteFile.getBidSize(i), quoteFile.getAskPrice(i), quoteFile.getAskSize(i)]])
                self._stackedQuotes = np.append(self._stackedQuotes, newRow, axis=0)
            
    # Trades
    def addCleanedTrades(self):
        for date in self._datesT:
            quoteFile = self._fm.getQuotesFile(date, self._ticker)
            tradeFile = self._fm.getTradesFile(date, self._ticker)
            cleaner = TAQCleaner( quoteFile, tradeFile)
            cleaner.cleanTrades()
            
            # Append the day data [TICKER, TIMESTAMP, PRICE, SIZE]
            length = tradeFile.getN()
            for i in range(0, length):
                newRow = np.array([[self._ticker, tradeFile.getTimestamp(i), tradeFile.getPrice(i), tradeFile.getSize(i)]])
                self._stackedTrades = np.append(self._stackedTrades, newRow, axis=0)
            
    # Returns the array of stacked cleaned trades   
    def getStackedTrades(self):
        return self._stackedTrades
    
    # Returns the array of stacked cleaned quotes
    def getStackedQuotes(self):    
        return self._stackedQuotes