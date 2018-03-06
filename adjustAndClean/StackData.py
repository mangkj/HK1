from impactModel.FileManager import FileManager
import numpy as np

class StackData(object):
    '''
    Class compiling the data on one ticker into two arrays.
    One numpy array, which rows are trades and columns are [DATE, TICKER, TIMESTAMP, PRICE, SIZE]
    A second one, which rows are quotes and columns are [DATE, TICKER, TIMESTAMP, BIDPRICE, BIDSIZE, ASKPRICE, ASKSIZE]
    '''

    def __init__(self, baseDir, startDate, endDate, ticker ):
        '''
        Uses the FileManager class to get the dates, and then loops through them to build the arrays
        via one call to the methods addQuotes and addTrades.
        '''
        self._fm = FileManager( baseDir )
        
        # Retrieve list of trading days for trades & quotes files
        self._datesT = self._fm.getTradeDates(startDate, endDate) # 20070620, 20070621, ...
        self._datesQ = self._fm.getQuoteDates(startDate, endDate)

        # Ticker searched
        self._ticker = ticker

        # Stacked data for this ticker
        self._stackedQuotes = np.empty((0,7))
        self._stackedTrades = np.empty((0,5))
        
    # Quotes
    def addQuotes(self):
        for date in self._datesQ:
            quoteFile = self._fm.getQuotesFile(date, self._ticker)
            
            # Append the day data [DATE, TICKER, TIMESTAMP, BIDPRICE, BIDSIZE, ASKPRICE, ASKSIZE]
            length = quoteFile.getN()
            for i in range(0, length):
                newRow = np.array([[date, self._ticker, int(quoteFile.getTimestamp(i)), float(quoteFile.getBidPrice(i)), float(quoteFile.getBidSize(i)), float(quoteFile.getAskPrice(i)), float(quoteFile.getAskSize(i))]])
                self._stackedQuotes = np.append(self._stackedQuotes, newRow, axis=0)
            
    # Trades
    def addTrades(self):
        for date in self._datesT:
            tradeFile = self._fm.getTradesFile(date, self._ticker)
            
            # Append the day data [DATE, TICKER, TIMESTAMP, PRICE, SIZE]
            length = tradeFile.getN()
            for i in range(0, length):
                newRow = np.array([[date, self._ticker, int(tradeFile.getTimestamp(i)), float(tradeFile.getPrice(i)), float(tradeFile.getSize(i))]])
                self._stackedTrades = np.append(self._stackedTrades, newRow, axis=0)
            
    # Returns the array of stacked adjusted trades   
    def getStackedTrades(self):
        return self._stackedTrades
    
    # Returns the array of stacked adjusted quotes
    def getStackedQuotes(self):    
        return self._stackedQuotes
        