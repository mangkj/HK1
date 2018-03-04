import gzip
import struct
import os.path
import itertools
from _collections import deque

class TAQQuotesReader(object):
    '''
    This reader reads an entire compressed binary TAQ quotes file into memory,
    uncompresses it, and gives its clients access to the contents of the file
    via a set of get methods.
    EDIT 1: The author has added several getters at the bottom of the class, as well
    as setters to allow price and volume adjustment (done in TAQAdjust).
    EDIT 2: The author has modified the data structures of the attributes of objects
    of this class from tuple to deque for two reasons: Adjustment on volume and price
    required these attributes to be mutable / Speed was needed in the treatment.
    '''

    # EDIT 2: deque
    def __init__(self, filePathName ):
        '''
        Do all of the heavy lifting here and give users getters for the
        results.
        '''
        self._filePathName = filePathName
        with gzip.open( self._filePathName, 'rb') as f:
            file_content = f.read()
            self._header = deque(struct.unpack_from(">2i",file_content[0:8]))
            
            # millis from midnight
            endI = 8 + ( 4 * self._header[1] )
            self._ts = deque(struct.unpack_from( ( ">%di" % self._header[ 1 ] ), file_content[ 8:endI ] ))
            startI = endI
            
            # bid size
            endI = endI + ( 4 * self._header[1] )
            self._bs = deque(struct.unpack_from( ( ">%di" % self._header[ 1 ] ), file_content[ startI:endI ] ))
            startI = endI

            # bid price
            endI = endI + ( 4 * self._header[1] )
            self._bp = deque(struct.unpack_from( ( ">%df" % self._header[ 1 ] ), file_content[ startI:endI ] ))
            startI = endI
            
            # ask size
            endI = endI + ( 4 * self._header[1] )
            self._as = deque(struct.unpack_from( ( ">%di" % self._header[ 1 ] ), file_content[ startI:endI ] ))
            startI = endI

            # ask price
            endI = endI + ( 4 * self._header[1] )
            self._ap = deque(struct.unpack_from( ( ">%df" % self._header[ 1 ] ), file_content[ startI:endI ] ))

    def getN(self):
        return self._header[1]
    
    def getSecsFromEpocToMidn(self):
        return self._header[0]
    
    def getMillisFromMidn( self, index ):
        return self._ts[ index ]

    def getAskSize( self, index ):
        return self._as[ index ]
    
    def getAskPrice( self, index ):
        return self._ap[ index ]

    def getBidSize( self, index ):
        return self._bs[ index ]
    
    def getBidPrice( self, index ):
        return self._bp[ index ]
    
    # EDIT 1: getters and setters
    def getTicker(self):
        return(os.path.basename(self._filePathName).split('_')[0])

    def getFilePath(self):
        return(self._filePathName)
    
    def setAskSize( self, index, val):
        self._as[ index ] = val
    
    def setAskPrice( self, index, val ):
        self._ap[ index ] = val

    def setBidSize( self, index, val ):
        self._bs[ index ] = val
    
    def setBidPrice( self, index, val ):
        self._bp[ index ] = val
        
    def getAskPriceSlice(self, start, end):
        return list(itertools.islice(self._ap, start, end))

    def getBidPriceSlice(self, start, end):
        return list(itertools.islice(self._bp, start, end))

    def cleanList(self, indices):
        for i in sorted(indices, reverse=True): 
            del self._bp[i]
            del self._bs[i]
            del self._ap[i]
            del self._as[i]

        # Update fields
        self._header[1] = self._header[1] - len(indices)
        self._header[0] = self.getMillisFromMidn( 0 )