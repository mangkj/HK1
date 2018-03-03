import pandas as pd
import os.path

class TAQAdjust(object):
    '''
    Adjust prices, quotes and number of shares for corporate actions such as 
    stock splits/etc. by using the “Cumulative Factor to Adjust Prices” and 
    “Cumulative Factor to Adjust Shares/Vol” (see, “sp500.xlsx”). Note that
    if these factors did not change for a particular stock during the period,
    then no adjustment is necessary.
    '''

    def __init__(self, quoteFile, tradeFile, s_p500):
        '''
        quoteFile: TAQQuotesReader object
        tradeFile: TAQTradeReader object
        s_p500: String path to the s_p500.xlsx file
        '''
        # Instantiate attributes
        self._s_p500xls = pd.read_excel(open(s_p500,'rb'), sheet_name='WRDS')
        self._quoteFile = quoteFile
        self._tradeFile = tradeFile
        
        # Quotefile multipliers
        self._dateQ  = os.path.basename(os.path.dirname(quoteFile.getFilePath()))
        self._priceMultiplierQ = float(self._s_p500xls[(self._s_p500xls['Names Date'] == float(self._dateQ)) & (self._s_p500xls['Ticker Symbol'] == quoteFile.getTicker())]['Cumulative Factor to Adjust Prices'])
        self._volMultiplierQ = float(self._s_p500xls[(self._s_p500xls['Names Date'] == float(self._dateQ)) & (self._s_p500xls['Ticker Symbol'] == quoteFile.getTicker())]['Cumulative Factor to Adjust Shares/Vol'])
        
        # Tradefile multipliers
        self._dateT = os.path.basename(os.path.dirname(tradeFile.getFilePath()))
        self._priceMultiplierT = float(self._s_p500xls[(self._s_p500xls['Names Date'] == float(self._dateT)) & (self._s_p500xls['Ticker Symbol'] == tradeFile.getTicker())]['Cumulative Factor to Adjust Prices'])
        self._volMultiplierT = float(self._s_p500xls[(self._s_p500xls['Names Date'] == float(self._dateT)) & (self._s_p500xls['Ticker Symbol'] == tradeFile.getTicker())]['Cumulative Factor to Adjust Shares/Vol'])
        

    def adjustQuote(self):
        length = self._quoteFile.getN()
        for i in range(0, length):
            self._quoteFile.setAskPrice(i, self._priceMultiplierQ * self._quoteFile.getAskPrice(i))
            self._quoteFile.setAskSize(i, self._volMultiplierQ * self._quoteFile.getAskSize(i))
            self._quoteFile.setBidPrice(i, self._priceMultiplierQ * self._quoteFile.getBidPrice(i))
            self._quoteFile.setBidSize(i, self._volMultiplierQ * self._quoteFile.getBidSize(i))

    def adjustTrade(self):
        length = self._tradeFile.getN()
        for i in range(0, length):
            self._tradeFile.setPrice(i, self._priceMultiplierT * self._tradeFile.getPrice(i))
            self._tradeFile.setSize(i, self._volMultiplierT * self._tradeFile.getSize(i))

    def getVolMult(self):
        return(self._volMultiplierQ)
    
    def getPriceMult(self):
        return(self._priceMultiplierQ)
    
    # For the purpose of unit testing
    def setPriceMult(self, val):
        self._priceMultiplierQ = val
        self._priceMultiplierT = val
        
    # For the purpose of unit testing
    def setVolMult(self, val):
        self._volMultiplierQ = val
        self._volMultiplierT = val