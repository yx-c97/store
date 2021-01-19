import unittest
from  demo import Calculator
class TsetCalc3(unittest.TestCase):

    def testMul(self):
        c = Calculator()
        a = 9
        b = 10
        s = 90
        sum = c.mul(a, b)
        self.assertEquals(s, sum)

    def testMul1(self):
        c = Calculator()
        a = 8
        b = 10
        s = 80
        sum = c.mul(a, b)
        self.assertEquals(s, sum)

    def testMul2(self):
        c = Calculator()
        a = 7
        b = 10
        s = 70
        sum = c.mul(a, b)
        self.assertEquals(s, sum)

    def testMul3(self):
        c = Calculator()
        a = 6
        b = 10
        s = 60
        sum = c.mul(a, b)
        self.assertEquals(s, sum)

