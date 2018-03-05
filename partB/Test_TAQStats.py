import unittest
from dbReaders.TAQTradesReader import TAQTradesReader
from partB.TAQStats import TAQStats
from partB.xMinuteReturn import getXMinuteTradeReturns, getXMinuteMidQuoteReturns
from dbReaders.TAQQuotesReader import TAQQuotesReader

class Test_TAQStats(unittest.TestCase):

    def testXMinuteReturns(self):
        taqBaseDir = "/Users/canelbiryol/Documents/sampleTAQ/"
        filePathName = "trades/20070620/IBM_trades.binRT"
        
        data = TAQTradesReader( taqBaseDir + filePathName )
        #print( "%s" % (getXMinuteTradeReturns(data, 30)))

    def testStats(self):
        taqBaseDir = "/Users/canelbiryol/Documents/sampleTAQ/"
#         tradesFilePath = "trades/20070620/IBM_trades.binRT"
#         tradesData = TAQTradesReader( taqBaseDir + tradesFilePath )
#         tradesStats = TAQStats(tradesData)
        tradeStats = TAQStats(taqBaseDir, "IBM")
        print(tradeStats.getSampleLength())
        print(tradeStats.getNumofTrades())
        print(tradeStats.getNumofQuotes())
        print(tradeStats.getTradestoQuotes())
        
#         print (tradesStats.getMeanReturn(10, getXMinuteTradeReturns))
#         print (tradesStats.getStdReturn(10, getXMinuteTradeReturns))
#         print (tradesStats.getMedianAbsDev(10, getXMinuteTradeReturns))
#         print (tradesStats.getSkew(10, getXMinuteTradeReturns))
#         print (tradesStats.getKurtosis(10, getXMinuteTradeReturns))
#         print (tradesStats.get10largest(10, getXMinuteTradeReturns))
#         print (tradesStats.get10smallest(10, getXMinuteTradeReturns))
#         print ("/////////////////////////////////////////////////////////////////////////")
#         quotesFilePath = "quotes/20070620/IBM_quotes.binRQ"
#         quotesData = TAQQuotesReader( taqBaseDir + quotesFilePath )
#         quotesStats = TAQStats(quotesData)
#         print (quotesStats.getMeanReturn(10, getXMinuteMidQuoteReturns))
#         print (quotesStats.getStdReturn(10, getXMinuteMidQuoteReturns))
#         print (quotesStats.getMedianAbsDev(10, getXMinuteMidQuoteReturns))
#         print (quotesStats.getSkew(10, getXMinuteMidQuoteReturns))
#         print (quotesStats.getKurtosis(10, getXMinuteMidQuoteReturns))
#         print (quotesStats.get10largest(10, getXMinuteMidQuoteReturns))
#         print (quotesStats.get10smallest(10, getXMinuteMidQuoteReturns))
      

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testVWAP']
    unittest.main()