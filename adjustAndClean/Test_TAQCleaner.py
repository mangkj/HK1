import unittest
from dbReaders.TAQQuotesReader import TAQQuotesReader
from dbReaders.TAQTradesReader import TAQTradesReader

class Test_TAQCleaner(unittest.TestCase):
    '''TODO'''
    
    def test1(self):
        fileNameQ = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/data/sampleTAQ/sampleTAQ/quotes/20070621/MSFT_quotes.binRQ'
        fileNameT = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/data/sampleTAQ/sampleTAQ/trades/20070621/MSFT_trades.binRt'
        s_p500 = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/s_p500.xlsx'
        
        Qreader = TAQQuotesReader( fileNameQ )
        Treader = TAQTradesReader( fileNameT )
        
        # Initial quote check
        self.assertAlmostEquals( Qreader.getBidSize( Qreader.getN() - 1 ), 413, 2 )
        self.assertAlmostEquals( Qreader.getAskSize( Qreader.getN() - 1 ), 1, 2 )
        self.assertAlmostEquals( Qreader.getAskPrice( Qreader.getN() - 1 ), 30.229, 2 )
        self.assertAlmostEquals( Qreader.getBidPrice( Qreader.getN() - 1 ), 30.219, 2 )

        # Initial trade check
        self.assertAlmostEquals( Treader.getPrice( Treader.getN() - 1 ), 30.219, 2 )
        self.assertAlmostEquals( Treader.getSize( Treader.getN() - 1 ), 12000, 2 )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1']
    unittest.main()