import unittest

class Test_TAQAdjust(unittest.TestCase):
    '''TODO'''

    def test1(self):
        fileName = '/Users/leonmaclin/Documents/sampleTAQ/trades/20070620/IBM_trades.binRT'
        reader = TAQTradesReader( fileName )
        print( reader.getN() )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1']
    unittest.main()