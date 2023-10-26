from random import randint, randrange
from calc import somar, subtrair, mult, div

# numero_1 = float(input("Digite o primeiro número: "))
# numero_2 = float(input("Digite o primeiro número: "))

# print(rd.randint(0, 34))
# num = rd.randint(0, 50)
# num2 = rd.randrange(0, 20, 4)

# print(num)
# print(num2)

# CALCULADORA

print("Calculadora v1.0")
print("Escolha uma das opções abaixo")
print("")

print("+ = SOMA")
print("- = SUBTRACAO")
print("* = MULTIPLICACAO")
print("/ = DIVISAO")

opcao = input("Escolha a opcao desejada: ")

opcoes = ('+. Adicao+', '-', '*', '/')

a = int(input("Digite o primeiro numero: "))
b = int(input("Digite o segundo numero: "))

if opcao == '+':    
    resultado = somar(a,b)
   # print("Soma: ")
elif opcao == '-':
    resultado = subtrair(a,b)
elif opcao == '*':
    resultado = mult(a,b)
elif opcao == '/':
    resultado = div(a,b)
else:
    print('Escolha errada!')
    print("Saindo...")

print(f'Resultado da {opcao}: {resultado}')
