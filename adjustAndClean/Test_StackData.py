import unittest
import pandas as pd
import numpy as np
from adjustAndClean.StackData import StackData

class Test_StackData(unittest.TestCase):
    '''
    This class tests the functionality of the methods addQuotes and addTrades of the class StackData.
    It works on the base directory provided by the user, and apply them to the IBM ticker.
    '''

    def test1(self):
        baseDir = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/data/sampleTAQ/sampleTAQ'
        s_p500 = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/s_p500.xlsx'
        
        ticker = "IBM"
        
        # Test if S&P ticker
        s_p500xls = pd.read_excel(open(s_p500,'rb'), sheet_name='WRDS')
        s_ptickers = np.unique((np.array(s_p500xls['Ticker Symbol'])).astype(str))
        s_ptickers = s_ptickers[:-1]
        
        if (not (ticker in s_ptickers)):
            print("Not a S&P ticker!")
            return

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