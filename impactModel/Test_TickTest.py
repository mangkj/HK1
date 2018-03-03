import unittest
from impactModel.TickTest import TickTest
from dbReaders.TAQTradesReader import TAQTradesReader

# Version 1802150758

class Test_TickTest(unittest.TestCase):


    def test_classify(self):
        tickTest = TickTest()
        self.assertTrue( tickTest.classify( 100 ) == 0 )
        self.assertTrue( tickTest.classify( 100 ) == 0 )
        self.assertTrue( tickTest.classify( 101 ) == 1 )
        self.assertTrue( tickTest.classify( 101 ) == 1 )
        self.assertTrue( tickTest.classify( 102 ) == 1 )
        self.assertTrue( tickTest.classify( 101 ) == -1 )
        self.assertTrue( tickTest.classify( 101 ) == -1 )
        self.assertTrue( tickTest.classify( 102 ) == 1 )
        
    def test_classifyAll(self):
        filePathName = "/Users/leonmaclin/Documents/sampleTAQ/trades/20070620/IBM_trades.binRT"        
        data = TAQTradesReader(filePathName)
        tickTest = TickTest()
        startOfDay = 18 * 60 * 60 * 1000 / 2
        endOfDay = startOfDay + ( 13 * 60 * 60 * 1000 / 2 )
        classifications = tickTest.classifyAll( data, startOfDay, endOfDay )
        # To see the first 10 prices, enable Window > Show view > Expressions
        # In the Expressions window, paste: list(map(lambda i: data.getPrice(i), range( 0, 10 )))
        self.assertTrue( data.getPrice(1) < data.getPrice(0) )
        # Each classification is a tuple containing timestamp, price, and classification
        self.assertTrue( classifications[ 0 ][ 2 ] == 0 ) # 1st good price has a classification of 0
        self.assertTrue( classifications[ 1 ][ 2 ] == -1 ) # 2nd good price has a classification of -1
        # We now look at the back of the queue
        self.assertTrue( classifications[-4][1] < classifications[-3][1] ) # 4th last price is less than 3rd last price
        self.assertAlmostEqual( classifications[-3][1], classifications[-2][1], 0.00001 ) # 3rd last price and 2nd last price are the same
        self.assertAlmostEqual( classifications[-2][1], classifications[-1][1], 0.00001 ) # 2nd last price and last price are the same
        self.assertTrue( classifications[-3][2] == 1 )
        self.assertTrue( classifications[-2][2] == 1 )
        self.assertTrue( classifications[-1][2] == 1 )
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.testName']
    unittest.main()