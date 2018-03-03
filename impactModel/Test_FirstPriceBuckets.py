import unittest
from impactModel.FirstPriceBuckets import FirstPriceBuckets
from dbReaders.TAQTradesReader import TAQTradesReader

class Test_FirstPriceBuckets(unittest.TestCase):


    def testConstructor(self):
        
        startTS = None
        endTS = None
        numBuckets = 2
        baseDir = "/Users/leonmaclin/Documents/sampleTAQ/"
        fileName = "trades/20070620/IBM_trades.binRT"
        data = TAQTradesReader( baseDir + fileName )
        
        fpb = FirstPriceBuckets( data, numBuckets, startTS, endTS )
        self.assertTrue( fpb.getN() == 2 )
        self.assertTrue( fpb.getTimestamp( 0 ) == 34241000 and fpb.getTimestamp( 1 ) == 45901000 )
        self.assertTrue( fpb.getPrice( 0 ) > ( 106.5 - 0.0001 ) and fpb.getPrice( 0 ) < ( 106.5 + 0.0001 ) )
        self.assertTrue( fpb.getPrice( 1 ) > ( 106.73999786376953 - 0.0001 ) and fpb.getPrice( 1 ) < ( 106.73999786376953 + 0.0001 ) )
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()