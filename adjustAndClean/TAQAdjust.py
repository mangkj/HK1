import gzip
import struct
import pandas as pd

class TAQAdjust(object):
    '''TOCHECK'''
    '''
    Adjust prices, quotes and number of shares for corporate actions such as 
    stock splits/etc. by using the “Cumulative Factor to Adjust Prices” and 
    “Cumulative Factor to Adjust Shares/Vol” (see, “sp500.xlsx”). Note that
    if these factors did not change for a particular stock during the period,
    then no adjustment is necessary.
    '''

    def __init__(self, date, quoteFile, tradeFile, s_p500):
        '''
        '''
        #spSheet = s_p500.parse("WRDS")
        self._quoteFile = quoteFile
        self._tradeFile = tradeFile
        self._priceMultiplier = float(s_p500[s_p500['Names Date'] == date]['Cumulative Factor to Adjust Prices'])
        self._volMultiplier = float(s_p500[s_p500['Names Date'] == date]['Cumulative Factor to Adjust Shares/Vol'])


    def adjustQuote(self):
        length = self._quoteFile.getN()
        for i in range(0, length):
            self._quoteFile.setAskPrice(i, self._priceMultiplier * self._quoteFile.getAskPrice())
            self._quoteFile.setAskSize(i, self._volMultiplier * self._quoteFile.getAskSize())
            self._quoteFile.setBidPrice(i, self._priceMultiplier * self._quoteFile.getBidPrice())
            self._quoteFile.setBidSize(i, self._volMultiplier * self._quoteFile.getBidSize())

    def adjustTrade(self):
        length = self._tradeFile.getN()
        for i in range(0, length):
            self._tradeFile.setPrice(i, self._priceMultiplier * self._tradeFile.getPrice())
            self._tradeFile.setSize(i, self._volMultiplier * self._tradeFile.getSize())