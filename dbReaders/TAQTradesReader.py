import gzip
import struct

class TAQTradesReader(object):
    
    '''
    This reader reads an entire compressed binary TAQ trades file into memory,
    uncompresses it, and gives its clients access to the contents of the file
    via a set of get methods.
    '''


    def __init__(self, filePathName ):
        '''
        Do all of the heavy lifting here and give users getters for the results.
        '''
        self.filePathName = filePathName
        with gzip.open( filePathName, 'rb') as f:
            file_content = f.read()
            self._header = struct.unpack_from(">2i",file_content[0:8])
            endI = 8 + ( 4 * self._header[1] )
            self._ts = struct.unpack_from( ( ">%di" % self._header[ 1 ] ), file_content[ 8:endI ] )
            startI = endI
            endI = endI + ( 4 * self._header[1] )
            self._s = struct.unpack_from( ( ">%di" % self._header[ 1 ] ), file_content[ startI:endI ] )
            startI = endI
            endI = endI + ( 4 * self._header[1] )
            self._p = struct.unpack_from( ( ">%df" % self._header[ 1 ] ), file_content[ startI:endI ] )

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
    
    # @lguigo
    
    def setPrice(self, index, val):
        self._p[ index ] = val
    
    def setSize(self, index, val):
        self._s[ index ] = val