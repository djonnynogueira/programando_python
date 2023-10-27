"""
 ===> Laboratório 3 - página 118 <===
    
    Em um clube, o valor da entrada varia de acordo com a idade do associado.
    Os critérios são:
    
    => Até 17 anos - R$ 50,00; 
    => Entre 18 e 59 anos - R$ 60,00;
    => A partir de 60 anos - R$ 20,00.
    
    O programa deve apresentar o nome do associado e o valor do ingresso a ser pago.
    
"""

nome_associado = input("Digite o nome do associado: ")
idade_associado = int(input("Digite a idade do associado: "))
valor_entrada = 0

if idade_associado < 17:
    # valor_entrada = 50
    print(f"Nome do associado: {nome_associado} \nValor da entrada: R$50.00")
elif idade_associado >= 18 and idade_associado < 60:
    print(f"Nome do associado: {nome_associado} \nValor da entrada: R$60.00")
else:
     print(f"Nome do associado: {nome_associado} \nValor da entrada: R$20.00")
     

# if idade_associado < 17:
#     valor_entrada = 50
#     print(f"Nome do associado: {nome_associado} \nValor da entrada: R${valor_entrada}")
# elif idade_associado >= 18 and idade_associado < 60:
#     valor_entrada = 60
#     print(f"Nome do associado: {nome_associado} \nValor da entrada: R${valor_entrada}")
# else:
#     valor_entrada = 20
#     print(f"Nome do associado: {nome_associado} \nValor da entrada: R${valor_entrada}")

'''
lab 4

'''

ano = int(input("Coloque o ano de referencia "))

if ano % 4 == 0:
    print(f"Ano bissexto, Dias de fevereiro: 29")
else:
    print(f"Dias de fevereiro: 28")