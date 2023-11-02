from testes import Teste01, Teste02

def soma(a, b):
    return a + b


# resultado = soma(3,6) == 9

resultado_soma = soma(3,6)

try:
    assert resultado_soma == 9, "Era para ser 9 no resultado!"
except TypeError as e:
    print(f"Erro: {e}")
    # raise TypeError("Erro ao passar o valor")

except ValueError as e:
    print(f'Erro: {e}')

except AssertionError as e:
    print(f"Erro de Teste: {e}")
    
# print("Passou do teste")

import unittest


unittest.main()