from calgrade import calGrade
import unittest


class Test_Calgrade(unittest.TestCase):
    def testSumFunctionA(self):
        self.assertEqual(calGrade(80),'A')
    
    def testSumFunctionB(self):
        self.assertEqual(calGrade(70),'B')

    def testSumFunctionC(self):
        self.assertEqual(calGrade(60),'C')

    def testSumFunctionD(self):
        self.assertEqual(calGrade(50),'D')

    def testSumFunctionF(self):
        self.assertEqual(calGrade(49),'F')