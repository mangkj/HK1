import unittest
from impactModel.LastPriceBuckets import LastPriceBuckets
from dbReaders.TAQTradesReader import TAQTradesReader

class Test_LastPriceBuckets(unittest.TestCase):

    def testConstructor(self):
        
        startTS = None
        endTS = None
        numBuckets = 2
        baseDir = '/Users/leonmaclin/Documents/sampleTAQ/'
        fileName = 'trades/20070620/IBM_trades.binRT'
        data = TAQTradesReader( baseDir + fileName )
        
        fpb = LastPriceBuckets( data, numBuckets, startTS, endTS )
        self.assertTrue( fpb.getN() == 2 )
        self.assertTrue( fpb.getTimestamp( 0 ) == 45896000 and fpb.getTimestamp( 1 ) == 57599000 )
        self.assertTrue( fpb.getPrice( 0 ) > ( 106.72000122070312 - 0.0001 ) and fpb.getPrice( 0 ) < ( 106.72000122070312 + 0.0001 ) )
        self.assertTrue( fpb.getPrice( 1 ) > ( 106.0 - 0.0001 ) and fpb.getPrice( 1 ) < ( 106.0 + 0.0001 ) )
        
        print ("Finished")
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()