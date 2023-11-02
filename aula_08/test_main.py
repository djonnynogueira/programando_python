import unittest
from main import soma
from testes import Teste01, Teste02

class TesteMain(unittest.TestCase):
    def testar_funcao_Main(self):
        self.assertEqual(soma(2,3), 5, "Errado os dados passados")
        
        
if __name__ == "__main__":
    unittest.main()