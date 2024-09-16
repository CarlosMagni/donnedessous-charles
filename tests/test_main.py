import unittest
from donnedessouscharles.main import donne_des_sous, compte_en_banque

class MyTestCase(unittest.TestCase):
    def test_something(self):
        compte_en_banque = donne_des_sous(8,10)
        self.assertEquals(18, compte_en_banque)

if __name__ == '__main__':
    unittest.main()
