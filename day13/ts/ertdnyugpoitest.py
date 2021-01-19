import unittest
from  demo import Calculator
class TsetCalc4(unittest.TestCase):
    def testDiv(self):
        c = Calculator()
        a=9
        b=10
        s=0.9
        sum=c.div(a,b)
        self.assertEquals(s,sum)

    def testDiv1(self):
        c = Calculator()
        a=8
        b=10
        s=0.8
        sum=c.div(a,b)
        self.assertEquals(s,sum)


    def testDiv2(self):
        c = Calculator()
        a=7
        b=10
        s=0.7
        sum=c.div(a,b)
        self.assertEquals(s,sum)

    def testDiv3(self):
        c = Calculator()
        a=6
        b=10
        s=0.6
        sum=c.div(a,b)
        self.assertEquals(s,sum)

