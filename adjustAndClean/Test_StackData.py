import unittest
from adjustAndClean.StackData import StackData

class Test_StackData(unittest.TestCase):
    '''
    This class tests the functionality of the methods addQuotes and addTrades of the class StackData.
    It works on the base directory provided by the user, and apply them to the IBM ticker.
    '''

    def test1(self):
        baseDir = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/data/sampleTAQ/sampleTAQ'
        
        ticker = "IBM"

        # Calls to StackData methods
        loopStack = StackData( baseDir, "20070101" , "20070909", ticker )
        loopStack.addTrades()
        loopStack.addQuotes()
        
        # Visualization
        print(loopStack.getStackedTrades())
        print(loopStack.getStackedQuotes())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1']
    unittest.main()