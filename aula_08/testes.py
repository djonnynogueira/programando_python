import unittest
from main import soma

class Teste01(unittest.TestCase): #herança
    
    def teste_soma(self):
        self.assertEqual(soma(3,6), 13, 'Era pra ser 9')
        
        
        
class Teste02(unittest.TestCase): #herança
    
    def teste_adcao(self):
        self.assertEqual(soma(3,6), 13, 'deu bug')
        
if __name__ ==  "__main__":
    unittest.main()