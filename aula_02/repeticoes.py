lista = [1,2,3,5,6]

# print(lista)

tamanho = len(lista)
# print(tamanho)

# print(range(2, tamanho))

# for i in lista:
#     pass
#     print(i)
    
# for x in range(2,5):
#     print(x)
        
# cliente = {}

# for x in [1,'j',3]:
#     print(x)
    
    
# for x in ['Djonny','Nogueira']:
#     cliente['Info'] = x
    
# print(cliente)

# for chave, valor in [('nome', 'Djonny'), ('Sobrenome', 'Nogueira')]:
#     cliente[chave] =  valor
#     # break
# print(cliente)

# # for x in range(1, 10,3):
# #     print(x)
    
    
# for numero in range(20):
#     if numero % 2 == 0:
#         print("Par")
#     else:
#         print(numero)
    
    
# numero = int(input('Digite um inteiro: '))
# if (numero%2) == 0:
#     print("Par")
# else:
#     print("Ímpar")
    
    
# while
x = 0
while x < 2:
    print("Menor que 2")
    x += 1
    
multipo_5 = False
tentativa = 0
while multipo_5 == False:
    saque = int(input("Coloque um valor multiplo de 5: "))
    
    if saque % 5 == 0:
        multipo_5 = True
    else:
        tentativa += 1
        
        if tentativa == 3:
            saque =  'acabou a tentativa'
        break
    
        print('Coloque um valor multiplo de 5, tente novamente9 ')
    
print(saque)