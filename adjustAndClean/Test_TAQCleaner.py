import unittest
from dbReaders.TAQQuotesReader import TAQQuotesReader
from dbReaders.TAQTradesReader import TAQTradesReader
from adjustAndClean.TAQCleaner import TAQCleaner

class Test_TAQCleaner(unittest.TestCase):
    '''TODO'''
    
    def test1(self):
        fileNameQ = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/data/sampleTAQ/sampleTAQ/quotes/20070621/MSFT_quotes.binRQ'
        fileNameT = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/data/sampleTAQ/sampleTAQ/trades/20070621/MSFT_trades.binRt'
        
        Qreader = TAQQuotesReader( fileNameQ )
        Treader = TAQTradesReader( fileNameT )
        
        # Initial quote check
        self.assertAlmostEquals( Qreader.getAskPrice( Qreader.getN() - 1 ), 30.229, 2 )
        self.assertAlmostEquals( Qreader.getBidPrice( Qreader.getN() - 1 ), 30.219, 2 )

        # Initial trade check
        self.assertAlmostEquals( Treader.getPrice( Treader.getN() - 1 ), 30.219, 2 )
        
        # Perturbation of the last midprice by a factor 10000
        Qreader.setAskPrice(Qreader.getN() - 1, 10000 * Qreader.getAskPrice(Qreader.getN() - 1))
        Qreader.setBidPrice(Qreader.getN() - 1, 10000 * Qreader.getBidPrice(Qreader.getN() - 1))
        
        # Perturbation of the last trade price by a factor 5000
        Treader.setPrice(Treader.getN() - 1, 5000 * Treader.getPrice(Treader.getN() - 1))

        # Check the execution of the perturbations
        self.assertAlmostEquals( Qreader.getAskPrice( Qreader.getN() - 1 ), 302299.99542, 2 )
        self.assertAlmostEquals( Qreader.getBidPrice( Qreader.getN() - 1 ), 302199.99313, 2 )
        self.assertAlmostEqual( Treader.getPrice( Treader.getN() - 1), 151099.99656, 2 )
        
        cleaner = TAQCleaner( Qreader, Treader)
        
        # Execute quote cleaning
        print(Qreader.getN())
        cleaner.cleanQuotes()
        print(Qreader.getN())
        
        # Execute trade cleaning
        print(Treader.getN())
        cleaner.cleanTrades()
        print(Treader.getN())
        
if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1']
    unittest.main()