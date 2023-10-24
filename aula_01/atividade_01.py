#
#ATIVIDADE 01 
#""" EXERCICIO 01
#    
#    Escrever um programa em Python que solicite informações de três pessoas, 
#    como nome, idade, peso e altura. Apresentar na tela estas informações de modo que permaneçam alinhados verticalmente. 
#    Usar a formatação de interpolação.
#"""
#
## nome = input("Qual é o seu nome? ")
#try:
#    idade = int(input("Qual é a sua idade? "))
#except:
#    print("Dados informado errado")
## peso = input("Qual é o seu peso? ")
## altura = input("Qual é a sua altura? ")
#
##print("="*30)
##print(f"Nome:  {nome} ")
##print(f"Idade:  {idade} ")
##print(f"Peso:  {peso} ")
##print(f"Altura:  {altura} ")
## print(f"Dados: \n Nome: {nome} \n Idade: {idade} \n Peso: {peso} \n Altura: {altura}")
#
## CONDICIONAL
#if 0 == 1:
#    pass
#    # print(" verdadeira")
#else:
#    pass
#    # print("Falsa")
#    
## < 7 => Reprovado | >7.9 => Aprovado | Entre 7 - 7.9 Recuperacao
#
#nota = 6.9
#
## if nota > 7.9:
##     print("Aprovado!")
## elif nota >= 7:
##     print("Recuperacao")
## else:
##     print("Reprovado!")
#
#
#print("Aprovado") if nota > 7 else print("Reprovado")

nome_2 = input("Qual é o seu nome? ")
idade_2 = int(input("Qual é a sua idade?"))
peso_2 = input("Qual é o seu peso? ")
altura_2 = input("Qual é a sua altura? ")

print(f"Nome 02: {nome_2} \n Idade 02: {idade_2} \n Peso 02: {peso_2} \n Altura 02: {altura_2}")
print("="*30)

#print(f"Nome 03: {pessoa_3[0]} \n Idade 03: {pessoa_3[1]} \n Peso 03: {pessoa_3[2]} \n Altura 03: {pessoa_3[3]}")