import unittest
from  demo import Calculator
class TsetCalc(unittest.TestCase):
    def testAdd(self):
        c = Calculator()
        a=9
        b=10
        s=19
        sum=c.add(a,b)
        self.assertEquals(s,sum)

    def testAdd1(self):
        c = Calculator()
        a=9
        b=10
        s=19
        sum=c.add(a,b)
        self.assertEquals(s,sum)
    def testAdd2(self):
        c = Calculator()
        a=9
        b=10
        s=19
        sum=c.add(a,b)
        self.assertEquals(s,sum)

    def testAdd3(self):
        c = Calculator()
        a=9
        b=10
        s=19
        sum=c.add(a,b)
        self.assertEquals(s,sum)




