import unittest
from dbReaders.TAQQuotesReader import TAQQuotesReader
from dbReaders.TAQTradesReader import TAQTradesReader
from adjustAndClean.TAQAdjust import TAQAdjust

class Test_TAQAdjust(unittest.TestCase):
    ''' Class testing the correction of adjustment operations on prices and volumes.
        On the sample data given, both price and volume multipliers were 1.0.
        So for the sake of example we modified them to .5 and .25 respectively.
        Setters have been introduced in TAQAdjust only for that purpose.'''

    def test1(self):
        fileNameQ = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/data/sampleTAQ/sampleTAQ/quotes/20070621/MSFT_quotes.binRQ'
        fileNameT = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/data/sampleTAQ/sampleTAQ/trades/20070621/MSFT_trades.binRt'
        s_p500 = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/s_p500.xlsx'
        
        Qreader = TAQQuotesReader( fileNameQ )
        Treader = TAQTradesReader( fileNameT )
        adjuster = TAQAdjust( Qreader, Treader, s_p500 )
        
        # Initial quote check
        self.assertAlmostEquals( Qreader.getBidSize( Qreader.getN() - 1 ), 413, 2 )
        self.assertAlmostEquals( Qreader.getAskSize( Qreader.getN() - 1 ), 1, 2 )
        self.assertAlmostEquals( Qreader.getAskPrice( Qreader.getN() - 1 ), 30.229, 2 )
        self.assertAlmostEquals( Qreader.getBidPrice( Qreader.getN() - 1 ), 30.219, 2 )

        # Initial trade check
        self.assertAlmostEquals( Treader.getPrice( Treader.getN() - 1 ), 30.219, 2 )
        self.assertAlmostEquals( Treader.getSize( Treader.getN() - 1 ), 12000, 2 )
        
        # On the sample data given, both price and volume multipliers were 1.0.
        # So for the sake of example we modified them.
        adjuster.setPriceMult(0.5)
        adjuster.setVolMult(0.25)
        adjuster.adjustQuote()
        adjuster.adjustTrade()
        
        # Quote modification check
        self.assertAlmostEquals( Qreader.getBidSize( Qreader.getN() - 1 ), 103.25, 2 )
        self.assertAlmostEquals( Qreader.getAskSize( Qreader.getN() - 1 ), 0.25, 2 )
        self.assertAlmostEquals( Qreader.getAskPrice( Qreader.getN() - 1 ), 15.114, 2 )
        self.assertAlmostEquals( Qreader.getBidPrice( Qreader.getN() - 1 ), 15.109, 2 )

        # Trade modification check
        self.assertAlmostEquals( Treader.getPrice( Treader.getN() - 1 ), 15.109, 2 )
        self.assertAlmostEquals( Treader.getSize( Treader.getN() - 1 ), 3000.0, 2 )
        

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1']
    unittest.main()