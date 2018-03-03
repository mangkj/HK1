import unittest
from dbReaders.TAQTradesReader import TAQTradesReader
from impactModel.VWAP import VWAP

class Test_VWAP(unittest.TestCase):

    def testVWAP(self):
        taqBaseDir = "/Users/leonmaclin/Documents/sampleTAQ/"
        filePathName = "trades/20070620/IBM_trades.binRT"
        start930 = 19 * 60 * 60 * 1000 / 2
        end4 = 16 * 60 * 60 * 1000
        vwap = VWAP( TAQTradesReader( taqBaseDir + filePathName ), start930, end4 )
        print( "There were %d trades and a VWAP price of %f" % ( vwap.getN(), vwap.getVWAP()))


if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testVWAP']
    unittest.main()