import unittest

class Test_TAQCleaner(unittest.TestCase):
    '''TODO'''
    
    def test1(self):
        # This is where I keep my test directory. Please
        # change this location for your own test.
        baseDir = '/Users/leonmaclin/Documents/sampleTAQ/'
        # This is the file I will open and read for this test
        fileName = 'quotes/20070620/IBM_quotes.binRQ'
        
        reader = TAQQuotesReader( baseDir + fileName )
        
        # Using previously tested readers, test for expected values
        
        # Header records
        # Number of records
        self.assertEquals( reader.getN(), 68489 )
        # Seconds from Epoc
        self.assertEquals( reader.getSecsFromEpocToMidn(), 1182312000 )
        
        # End records
        self.assertEquals( reader.getMillisFromMidn( reader.getN() - 1 ), 57599000 )
        self.assertEquals( reader.getBidSize( reader.getN() - 1 ), 20 )
        self.assertEquals( reader.getAskSize( reader.getN() - 1 ), 16 )
        self.assertAlmostEquals( reader.getAskPrice( reader.getN() - 1 ), 106.03, 3 )
        self.assertAlmostEquals( reader.getBidPrice( reader.getN() - 1 ), 106, 3 )
        '''
            The following is taken from test R-based file readers for
            comparison:
            
            Start of file:
            Header
            > zz$h
            $s
            [1] 1182312000
            $n
            [1] 68489
             
            > colnames(zz$r)
            [1] "m"  "bs" "bp" "as" "ap"
            
            Records
             > zz$r[1,"m"]
                   m 
            34241000 
            > zz$r[1,"bs"]
            bs 
             4 
            > zz$r[1,"bp"]
                bp 
            106.42 
            > zz$r[1,"as"]
             as 
            252 
            > zz$r[1,"ap"]
               ap 
            106.5 
            >
            
            End of file:
            > zz$r[,"m"][zz$h$n]
            [1] 57599000
            > zz$r[,"bs"][zz$h$n]
            [1] 20
            > zz$r[,"bp"][zz$h$n]
            [1] 106
            > zz$r[,"ap"][zz$h$n]
            [1] 106.03
            > zz$r[,"as"][zz$h$n]
            [1] 16
            > 
            
            
        '''

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1']
    unittest.main()