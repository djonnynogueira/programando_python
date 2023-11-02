"""Escrever uma função que receba como parâmetro o valor da base de cálculo do salário, 
e retorne o imposto de renda correspondente.

Sugestão: Usar tuplas para armazenar as faixas de valores.

"""
from srv import Colaborador


def start():
    nome = input('Nome do colaborador: ')

    x = 0
    
    while x < 1:
        try:
            salario = float(input('Salario do colaborador: '))
            cliente = Colaborador(nome, salario)
            
            x += 1
        except:
            pass
        
    imposto = cliente.calcular_irpf()
    
    print(f"Colaborador: {cliente.colaborador}")
    print(f"Salario: R${cliente.salario:.2f}")
    print(f"Imposto: R${imposto:.2f}")
    
    input("Cliquem em enter para fechar...")

if __name__ == "__main__":
    start()