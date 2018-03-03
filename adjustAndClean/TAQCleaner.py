import gzip
import struct

class TAQCleaner(object):
    '''TODO'''
    '''
    Cleans the adjusted TAQ Data.
    The method gives the option to store the cleaned data to files.
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
    
    