import gzip
import struct
import os.path
import itertools
from _collections import deque

class TAQTradesReader(object):
    
    '''
    This reader reads an entire compressed binary TAQ trades file into memory,
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
        Do all of the heavy lifting here and give users getters for the results.
        '''
        self._filePathName = filePathName
        with gzip.open( filePathName, 'rb') as f:
            file_content = f.read()
            self._header = deque(struct.unpack_from(">2i",file_content[0:8]))
            endI = 8 + ( 4 * self._header[1] )
            self._ts = deque(struct.unpack_from( ( ">%di" % self._header[ 1 ] ), file_content[ 8:endI ] ))
            startI = endI
            endI = endI + ( 4 * self._header[1] )
            self._s = deque(struct.unpack_from( ( ">%di" % self._header[ 1 ] ), file_content[ startI:endI ] ))
            startI = endI
            endI = endI + ( 4 * self._header[1] )
            self._p = deque(struct.unpack_from( ( ">%df" % self._header[ 1 ] ), file_content[ startI:endI ] ))

    def getN(self):
        return self._header[1]
    
    def getSecsFromEpocToMidn(self):
        return self._header[0]
    
    def getPrice( self, index ):
        return self._p[ index ]
    
    def getMillisFromMidn( self, index ):
        return self._ts[ index ]
    
    def getTimestamp(self, index ):
        return self.getMillisFromMidn( index ) # Compatibility 
    
    def getSize( self, index ):
        return self._s[ index ]
    
    # EDIT 1: getters and setters
    def getTicker(self):
        return(os.path.basename(self._filePathName).split('_')[0])

    def getFilePath(self):
        return(self._filePathName)
    
    def setPrice(self, index, val):
        self._p[ index ] = val
    
    def setSize(self, index, val):
        self._s[ index ] = val

    def getPriceSlice(self, start, end):
        return list(itertools.islice(self._p, start, end))
