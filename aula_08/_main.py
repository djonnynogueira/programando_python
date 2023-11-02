# # REQUIREMENTS
# # pip freeze > requirements.txt

# # Criando venv: py -m venv venv
# # Habilitando venv: . .\venv\Scripts\Activate
# # Desativando venv: deactivate

# import unittest
# from testes import Teste01, Teste02

# def soma(a, b):
#         return a + b

# # resultado = soma(3, 6) == 9

# # print(resultado)


# resultado_soma = soma(3, 6)
# try:
#     assert resultado_soma == 9, "Era para ser 9 no resultado!" 
# except TypeError as e:
#     print(f'Erro: {e}')
#     # raise ValueError("Erro ao passar o valor")
#     # print("Não era 9!")
# except ValueError as e:
#     print(f'Erro: {e}')

# except AssertionError as e:
#     print(f'Erro de Teste: {e}')
    
# # print("Passou do teste!")

# # from testes import Teste01

# # TESTE UNITARIO


# # class Teste01(unittest.TestCase): # HERANÇA
    
# #     def test_soma(self):
        
# #         self.assertEqual(soma(3,6), 19, 'Era para ser 9')

# if __name__ == "__main__":
#     unittest.main()


    
    