import numpy as np
from dbReaders.TAQTradesReader import TAQTradesReader
from dbReaders.TAQQuotesReader import TAQQuotesReader
from astropy.stats import median_absolute_deviation
from impactModel.FileManager import FileManager
from scipy.stats import skew, kurtosis
import heapq
from partB.xMinuteReturn import getXMinuteTradeReturns, getXMinuteMidQuoteReturns

class TAQStats(object):
    '''
    This class calculates the volume weighted average price between
    a start time and an end time (exclusive).
    '''

    def __init__( self, basedir, ticker):
        '''
        This does all the processing and gives the client access to the
        results via getter methods.
        '''
        
        startDateString = "20070620"
        endDateString = "20070920"
        
        self._fm = FileManager(basedir)
        self._ticker = ticker
        self._tradeDates = self._fm.getTradeTickerDates(startDateString, endDateString, ticker )
        self._quoteDates = self._fm.getQuoteTickerDates(startDateString, endDateString, ticker )
        
        # self._tradeData = 
        
        
#         self._data = data
        
        # Make sure data is in the right format
#         if ( data == None ) or ( data.getPrice == None ) or ( data.getTimestamp == None ) or ( data.getN == None ):
#             raise Exception( "Your data object must implement getPrice(i), getTimestamp(i), and getN() methods" ) 
    

    #part 2.a
    #how many days in the data for a ticker
    def getSampleLength(self):
        return len(self._tradeDates)
# #     
    #part 2.b
    def getNumofTrades(self):
        size = 0
        for date in self._tradeDates:
            file = self._fm.getTradesFile(date, self._ticker)
            size += file.getN()
        return size
# #     
    def getNumofQuotes(self):
        size = 0
        for date in self._quoteDates:
            file = self._fm.getQuotesFile(date, self._ticker)
            size += file.getN()
        return size
     
    def getTradestoQuotes(self):
        return self.getNumofTrades()/self.getNumofQuotes()
# #     
#     #part 2.c
#     
    def getMeanReturn(self, minutes, method):
        return np.mean( method( self._data, minutes ) ) * (minutes / (252 * 6.5 * 60))
     
    def getStdReturn(self, minutes, method):
        return np.std( method( self._data, minutes ) ) * np.sqrt((minutes / (252 * 6.5 * 60)))
     
    def getMedianAbsDev(self, minutes, method):
        return median_absolute_deviation( method( self._data, minutes ) ) * (minutes / (252 * 6.5 * 60))
     
    def getSkew(self, minutes, method):
        return skew( method( self._data, minutes ) )
     
    def getKurtosis(self, minutes, method):
        return kurtosis( method( self._data, minutes ) )
     
    def get10largest(self, minutes, method):
        return heapq.nlargest(10, method( self._data, minutes ) )
     
    def get10smallest(self, minutes, method):
        return heapq.nsmallest(10, method( self._data, minutes ) )
#     
#     