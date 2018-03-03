import unittest
from dbReaders.TAQTradesReader import TAQTradesReader

class Test_TAQTradesReader(unittest.TestCase):

    def test1(self):
        fileName = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/data/sampleTAQ/sampleTAQ/trades/20070620/IBM_trades.binRT'
        reader = TAQTradesReader( fileName )
        print( reader.getN() )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1']
    unittest.main()