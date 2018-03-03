import unittest
from impactModel.FileManager import FileManager

# Version 1802181651 
class Test_FileManager(unittest.TestCase):

    def test(self):
        baseDir = "/Users/leonmaclin/Documents/sampleTAQ"
        fm = FileManager( baseDir )
        
        # Define a range of date for which we will be retrieving 
        # actual trading days available in the TAQ database
        startDateString = "20070620"
        endDateString = "20070630"
        
        # Retrieve list of trading days for trades files
        dates = fm.getTradeDates(startDateString, endDateString) # 20070620, 20070621, ...
        # Retrieve list of trading days for quotes files
        dates = fm.getQuoteDates(startDateString, endDateString) # ..same...
        
        # dates[0] is the first date available
        # Retrieve list of tickers for trade files for that date
        tradeTickers = fm.getTradeTickers( dates[ 0 ] ) # IBM, MSFT, ...

        # dates[1] is the second date available
        # Retrieve list of tickers for quotes files for that date
        quoteTickers = fm.getQuoteTickers( dates[ 1 ] ) # IBM, MSFT, ...
        
        # Retrieve one IBM quotes file for the trade date 20070620
        ibm = fm.getQuotesFile( "20070620", "IBM" )
        
        # Retrieve one IBM trades file for the trade date 20070621
        ibm = fm.getTradesFile( "20070621", "IBM" )
        
        print( "Finished" )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test']
    unittest.main()