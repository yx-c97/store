import unittest
from  demo import Calculator
class TsetCalc1(unittest.TestCase):
    def testSub(self):
        c = Calculator()
        a = 9
        b = 10
        s = -1
        sum = c.sub(a, b)
        self.assertEquals(s, sum)

    def testSub1(self):
        c = Calculator()
        a = 9
        b = 10
        s = -1
        sum = c.sub(a, b)
        self.assertEquals(s, sum)

    def testSub2(self):
        c = Calculator()
        a = 9
        b = 10
        s = -1
        sum = c.sub(a, b)
        self.assertEquals(s, sum)

    def testSub3(self):
        c = Calculator()
        a = 9
        b = 10
        s = -1
        sum = c.sub(a, b)
        self.assertEquals(s, sum)


