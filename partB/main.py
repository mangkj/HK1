'''
Created on Mar 6, 2018

@author: canelbiryol
'''
from adjustAndClean.TAQAdjust import TAQAdjust
from adjustAndClean.TAQCleaner import TAQCleaner
from adjustAndClean.StackData import StackData

from partB.TAQStats import TAQStats

if __name__ == '__main__':
    baseDir = "/Users/canelbiryol/Documents/sampleTAQ/"
    startDate = "20070620"
    endDate = "20070622"
    ticker = 'IBM'
        
    stack = StackData(baseDir, startDate, endDate, ticker)
    stack.addTrades()
    stack.addQuotes()
    
    # Get results
    quotes = stack.getStackedQuotes()
    trades = stack.getStackedTrades()
    
#     print(quotes[0])
#     print(quotes[10])
#     print(quotes[-20])
#     print(quotes[-1])
#     exit(0)
    
    # Stats
    taqstats = TAQStats(trades, quotes)
    print("N Sample : {:d}".format(taqstats.getSampleLength()))
    print("N Trades : {:d}".format(taqstats.getNumofTrades()))
    print("N Quotes : {:d}".format(taqstats.getNumofQuotes()))
    print("Trades / Quotes : {:f}".format(taqstats.getTradestoQuotes()))
    
    seconds = 600
    print("Mean: {:E}".format(taqstats.getTradeMeanReturns(seconds)))
    print("STD: {:E}".format(taqstats.getTradeStdReturns(seconds)))
    print("Median Abs Dev: {:E}".format(taqstats.getTradeMedianAbsDev(seconds)))
    print("Skew: {:E}".format(taqstats.getTradeSkew(seconds)))
    print("Kurtosis: {:E}".format(taqstats.getTradeKurtosis(seconds)))
    print("10 largest: " + ', '.join(str(x) for x in taqstats.get10largestTrade(seconds)))
    print("10 smallest: " + ', '.join(str(x) for x in taqstats.get10smallestTrade(seconds)))
    # print(len(taqstats.getReturns(600)))
    