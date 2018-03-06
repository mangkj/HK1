import unittest
from adjustAndClean.LoopAndStackCleanAdjust import LoopAndSlackCleanAdjust

class Test_TAQAdjust(unittest.TestCase):
    ''' TODO '''

    def test1(self):
        '''TODO'''
        s_p500 = '/media/louis/DATA/documents/cours/NYU/SPRING_18/ATQS/HK1/s_p500.xlsx'
        loopAdjustClean = LoopAndSlackCleanAdjust( "20060101" , "20060909", s_p500 )

if __name__ == "__main__":
    #import sys;sys.argv = ['', 'Test.test1']
    unittest.main()