import unittest
import pandas as pd
import numpy as np
from adjustAndClean.LoopAndStackAdjust import LoopAndStackAdjust

class Test_loopAndStackAdjust(unittest.TestCase):
    ''' TODO '''

    def test1(self):
        '''TODO'''
        baseDir = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/data/sampleTAQ/sampleTAQ'
        s_p500 = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/s_p500.xlsx'
        
        ticker = "IBM"
        
        s_p500xls = pd.read_excel(open(s_p500,'rb'), sheet_name='WRDS')
        s_ptickers = np.unique((np.array(s_p500xls['Ticker Symbol'])).astype(str))
        s_ptickers = s_ptickers[:-1]
        
        # Test if S&P ticker
        if (not (ticker in s_ptickers)):
            print("Not a S&P ticker!")
            return

        loopAdjust = LoopAndStackAdjust( baseDir, "20070101" , "20070909", ticker, s_p500 )
        
        #loopAdjust.addAdjustedTrades()
        loopAdjust.addAdjustedQuotes()
        
        #print(loopAdjust.getStackedTrades())
        print(loopAdjust.getStackedQuotes())

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1']
    unittest.main()