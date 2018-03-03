import unittest
from impactModel.ReturnBuckets import ReturnBuckets
from dbReaders.TAQTradesReader import TAQTradesReader

class Test_ReturnBuckets(unittest.TestCase):

    def testName(self):
        startTS = 18 * 60 * 60 * 1000 / 2 # 930AM
        endTS = 16 * 60 * 60 * 1000 # 4PM
        numBuckets = 2
        baseDir = '/Users/leonmaclin/Documents/sampleTAQ/'
        fileName = 'trades/20070620/IBM_trades.binRT'
        data = TAQTradesReader( baseDir + fileName )
        returnBuckets = ReturnBuckets(data, startTS, endTS, numBuckets)
        self.assertTrue( returnBuckets.getN() == 2 )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()