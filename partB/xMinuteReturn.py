import numpy as np

def getXMinuteTradeReturns(data, seconds):
    delta = 1000 * seconds
        
    nRecs = data.getN()
    lastTs = data.getTimestamp(0)
    lastPrice = data.getPrice(0)
    TradeReturns = []
    
    for startI in range( 1, nRecs ):
        timestamp = data.getTimestamp( startI )
            
        # check this
        if timestamp > (lastTs + delta):
            lastTs = lastTs + delta
            newPrice = data.getPrice( startI )
                
            TradeReturns.append( np.log(newPrice/lastPrice) )
            lastPrice = newPrice
            lastTs = timestamp
        
    return TradeReturns

def getXMinuteMidQuoteReturns(data, minutes):
    delta = 1000 * 60 * minutes
        
    nRecs = data.getN()
    lastTs = data.getTimestamp(0)
    lastMidQuote = (data.getAskPrice( 0 ) + data.getBidPrice( 0 ))  / 2 
    midQuoteReturns = []
    for startI in range( 1, nRecs ):
        timestamp = data.getTimestamp( startI )
            
        # check this
        if timestamp > (lastTs + delta):
            lastTs = lastTs + delta
            #askPrice = data.getAskPrice( startI )
            #bidPrice = data.getBidPrice( startI ) 
            midQuote = (data.getAskPrice( startI ) + data.getBidPrice( startI ))  / 2 
            
            midQuoteReturns.append( np.log(midQuote/lastMidQuote) )
            lastMidQuote = midQuote
            lastTs = timestamp
        
    return midQuoteReturns
