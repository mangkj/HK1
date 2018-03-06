from impactModel.FileManager import FileManager
import pandas as pd
import numpy as np

class LoopAndSlackCleanAdjust(object):
    '''
    TODO
    '''

    def __init__(self, startDate, endDate, s_p500):
        '''
        TODO
        '''
        self._s_p500xls = pd.read_excel(open(s_p500,'rb'), sheet_name='WRDS')
        self._s_ptickers = np.unique((np.array(self._s_p500xls['Ticker Symbol'])).astype(str))
        self._s_ptickers = self._s_ptickers[:-1]
        
        print(self._s_ptickers)
        
        # Trades
        
        # Quotes