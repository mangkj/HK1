import numpy as np

class TAQCleaner(object):
    '''TODO'''
    '''
    Cleans the adjusted TAQ Data.
    The method gives the option to store the cleaned data to files.
    '''

    def __init__(self, quoteFile, tradeFile, storeRepo="no"):
        '''
        quoteFile: TAQQuotesReader object
        tradeFile: TAQTradeReader object
        storeRepo: String indicating if storage (yes) or not (no, or nothing)
        '''
        
        # Instantiate file attributes
        self._quoteFile = quoteFile
        self._tradeFile = tradeFile
        self._store = storeRepo
        
        # Suggested initial parameters, to calibrate
        self._k = 5
        self._gamma = 0.0005
        
    def cleanQuotes(self):
        # toRemove will keep track of indices to remove
        length = self._quoteFile.getN()
        toRemove = np.array()
        i = 0
        
        # Rolling parameters
        rollWindowMid = np.array()
        rollMeanMid = 0
        rollStdMid = 0
        
        # Min price difference in the timeframe 
        # It is likely to be the resolution parameter for the stock given the high number of transactions
        minTickDiff = min(np.min( abs(np.diff( np.array(self._quoteFile.getAskPriceSlice(1, length) - self._quoteFile.getAskPriceSlice(0, length - 1))))), np.min( abs(np.diff( np.array(self._quoteFile.getBidPriceSlice(1, length) - self._quoteFile.getBidPriceSlice(0, length - 1))))))
        
        # Midpoints
        midList = 0.5 * (np.array(self._quoteFile.getAskPriceSlice(0, length)) - np.array(self._quoteFile.getBidPriceSlice(0, length)))
        
        for i in range(0,length):
            leftIndex = i - self._k / 2
            rightIndex = i + self._k / 2
            
            # Set bounds of the rolling windows, taking into account limit cases
            if (leftIndex < 0):
                rightIndex -= leftIndex
                leftIndex = 0
            elif (rightIndex - length >= 0):
                leftIndex -= (rightIndex - length)
                rightIndex = length - 1

            # Compute rolling metrics
            rollWindowMid = midList[leftIndex:rightIndex]
            rollMeanMid = np.mean(rollWindowMid)
            rollStdMid = np.std(rollWindowMid)
            
            # Test criterion
            for j in range(0, self._k):
                if (abs(rollWindowMid[j] - rollMeanMid) < 2 * rollStdMid + self._gamma * minTickDiff):
                    toRemove = np.append(toRemove, leftIndex + j)
        
        self._quoteFile.cleanList(toRemove)
                    
    def cleanTrades(self):
        # toRemove will keep track of indices to remove
        length = self._tradeFile.getN()
        toRemove = np.array()
        i = 0
        
        # Rolling parameters
        rollWindow = np.array()
        rollMean = 0
        rollStd = 0
        
        # Min price difference in the timeframe 
        # It is likely to be the resolution parameter for the stock given the high number of transactions
        minTickDiff = np.min( abs(np.diff( np.array(self._tradeFile.getPriceSlice(1, length) - self._tradeFile.getPriceSlice(0, length - 1)))))
        
        windowTrade = self._tradeFile.getPriceSlice(0, length)
        
        for i in range(0,length):
            leftIndex = i - self._k / 2
            rightIndex = i + self._k / 2
            
            # Set bounds of the rolling windows, taking into account limit cases
            if (leftIndex < 0):
                rightIndex -= leftIndex
                leftIndex = 0
            elif (rightIndex - length >= 0):
                leftIndex -= (rightIndex - length)
                rightIndex = length - 1

            # Compute rolling metrics
            rollWindow = windowTrade[leftIndex:rightIndex]
            rollMean = np.mean(rollWindow)
            rollStd = np.std(rollWindow)
            
            # Test criterion
            for j in range(0, self._k):
                if (abs(rollWindow[j] - rollMean) < 2 * rollStd + self._gamma * minTickDiff):
                    toRemove = np.append(toRemove, leftIndex + j)

        self._tradeFile.cleanList(toRemove)

        