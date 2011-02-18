import unittest
from Aparelho import Aparelho

class TestAparelho(unittest.TestCase):

    def testCriacaodeAparelho(self):
        self.aparelho = Aparelho("sony", "vaio")

        self.assertEqual(self.aparelho.marca, 'sony')



        
            

if __name__== "__main__":
    unittest.main()
