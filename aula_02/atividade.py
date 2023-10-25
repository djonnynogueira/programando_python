"""
Laboratório 2
Escrever um programa que solicite ao usuário:

O nome de um funcionário;
Seu salário.

Se o salário for superior a R$ 5.000,00 ele terá um desconto de 10% 
sobre o que ultrapassar R$ 5.000,00. No final, apresentar:

O nome do funcionário;
O salário bruto;
O valor do desconto;
O salário líquido.

"""

nome = input("Informe o nome: ")
salario = float(input("Informe o salário: "))
desconto = 0.0
salario_liquido = salario

if salario > 5000:
    desconto = (salario - 5000) * (0.1)
    
salario_liquido = salario - desconto


print("="*30)
print(f"Nome Funcionário: {nome}")
print(f"Salario bruto: {salario}")
print(f"Valor do desconto: {desconto}")
print(f"Salario liquido: {salario_liquido}")