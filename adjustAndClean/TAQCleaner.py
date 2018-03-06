import numpy as np
import math

class TAQCleaner(object):
    '''TODO'''
    '''
    Cleans the adjusted TAQ Data.
    The method gives the option to store the cleaned data to files.
    '''

    def __init__(self, quoteFile, tradeFile):
        '''
        quoteFile: TAQQuotesReader object
        tradeFile: TAQTradeReader object
        '''
        
        # Instantiate file attributes
        self._quoteFile = quoteFile
        self._tradeFile = tradeFile
        
        # Suggested initial parameters, to calibrate
        self._k = 5
        self._gamma = 0.0005
        
    def cleanQuotes(self):
        # toRemove will keep track of indices to remove
        length = self._quoteFile.getN()
        toRemove = np.array([])
        i = 0
        
        # Rolling parameters
        rollWindowMid = np.array([])
        rollMeanMid = 0
        rollStdMid = 0
        
        # Min price difference in the timeframe 
        # It is likely to be the resolution parameter for the stock given the high number of transactions
        askIncrements = np.array(self._quoteFile.getAskPriceSlice(1, length)) - np.array(self._quoteFile.getAskPriceSlice(0, length - 1))
        bidIncrements = np.array(self._quoteFile.getBidPriceSlice(1, length)) - np.array(self._quoteFile.getBidPriceSlice(0, length - 1))
        minTickDiff = min(abs(np.min(askIncrements)), abs(np.min(bidIncrements)))
       
        # Midpoints
        midList = 0.5 * (np.array(self._quoteFile.getAskPriceSlice(0, length)) - np.array(self._quoteFile.getBidPriceSlice(0, length)))
        
        for i in range(0,length):
            leftIndex = math.floor(i - self._k / 2)
            rightIndex = math.floor(i + self._k / 2)
            
            # Set bounds of the rolling windows, taking into account limit cases
            if (leftIndex < 0):
                rightIndex -= leftIndex
                leftIndex = 0
            elif (rightIndex - length >= 0):
                leftIndex -= (rightIndex - length)
                rightIndex = length
            
            # Compute rolling metrics
            rollWindowMid = midList[leftIndex:rightIndex]
            rollMeanMid = np.mean(rollWindowMid)
            rollStdMid = np.std(rollWindowMid)

            #print("rollmean", rollMeanMid)
            #print("rollStd", rollStdMid)
            #print("rollWindow", rollWindowMid)
            #print("gamma", 3 * self._gamma * minTickDiff)
            
            # Test criterion
            for j in range(0, self._k):
                # TODO: Calibrate gamma and k
                if (abs(rollWindowMid[j] - rollMeanMid) >= 2 * rollStdMid + self._gamma * minTickDiff):
                    toRemove = np.append(toRemove, leftIndex + j)
                    print(rollWindowMid[j])
                    print(j)
                    
        toRemove = np.unique(toRemove)
        toRemove = toRemove.astype(int)
        print(toRemove)
        self._quoteFile.cleanList(toRemove)
                    
    def cleanTrades(self):
        # toRemove will keep track of indices to remove
        length = self._tradeFile.getN()
        toRemove = np.array([])
        i = 0
        
        # Rolling parameters
        rollWindow = np.array([])
        rollMean = 0
        rollStd = 0
        
        # Min price difference in the timeframe 
        # It is likely to be the resolution parameter for the stock given the high number of transactions
        tradeIncrements = np.array(self._tradeFile.getPriceSlice(1, length)) - np.array(self._tradeFile.getPriceSlice(0, length - 1))
        minTickDiff = abs(np.min(tradeIncrements))

        windowTrade = self._tradeFile.getPriceSlice(0, length)
        
        for i in range(0,length):
            leftIndex = math.floor(i - self._k / 2)
            rightIndex = math.floor(i + self._k / 2)
            
            # Set bounds of the rolling windows, taking into account limit cases
            if (leftIndex < 0):
                rightIndex -= leftIndex
                leftIndex = 0
            elif (rightIndex - length >= 0):
                leftIndex -= (rightIndex - length)
                rightIndex = length

            # Compute rolling metrics
            rollWindow = windowTrade[leftIndex:rightIndex]
            rollMean = np.mean(rollWindow)
            rollStd = np.std(rollWindow)

            # Test criterion
            for j in range(0, self._k):
                # TODO: Calibrate gamma and k
                if (abs(rollWindow[j] - rollMean) >= 2 * rollStd + self._gamma * minTickDiff):
                    toRemove = np.append(toRemove, leftIndex + j)

        toRemove = np.unique(toRemove)
        toRemove = toRemove.astype(int)
        print(toRemove)
        self._tradeFile.cleanList(toRemove)

    def storeCleanedTrades(self, directory):
        print("TODO")
        
    def storeCleanedQuotes(self, directory):
        print("TODO")
        