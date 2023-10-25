# numeros = 12, "Djonny"
#print(numeros)

# ===== COLECOES ===== (mutavel ou imutavel | retorna ou nao valores)

# LISTA => MUTAVEL (MUDA)

aluno = ['Djonny', 18, 1.97, True, [6,7,3,6,]]

#print(aluno)

# copo (classe)
# copo1 (Objeto)
# cor (Atributo)
# Armazenar liquido (metodo) acoes

#aluno.append("Aprovado") # adiciona
#print(aluno.append("Aprovado")) # não retorna nada
#print(aluno)

# aluno[4].append("Aprovado")

#print(aluno[4][2])
#aluno[4][2] = 8

# result = aluno.clear() #limpa a lista (não retorna)

# print(aluno)
# print(result)

#resultado = aluno[4].count(6) # retorna
#print(resultado)

# vezes = aluno[4].count(6) #retorna as vezes repetidas
# #aluno.pop(3) # remove o elemento da posição
# resultado = aluno.pop(3) # remove o elemento da posição (retorna)

# print(aluno)
# print(resultado)

# aluno.reverse()
# aluno.insert(1, "Python")
# print(aluno)

# def imprime_djonny(nome):
#     print(nome)
#     return "Nogueira"
# imprime_djonny("Djonny")

# resultado = imprime_djonny("Djonny")
# print(resultado)

# resultado = aluno.index(18) #posição do valor (retorna)
# print(aluno)
# print(resultado)

# print(type(aluno))  #list

# DICIONARIO => DICT ==== MUTAVEL

aluno_djonny = {
    'nome': 'Djonny', 
    'sobrenome': 'Nogueira', 
    'idade': 33,
    'altura': 1.92,
    'Notas': {
        'Bim1': 10,
        'Bim2': 40,
        'Bim3': 80,
        'Bim4': 50
    }
}

# print(aluno_djonny)
# print(aluno_djonny['nome'])
# print(aluno_djonny.get('nome'))

# nome = aluno_djonny['nome'] = 'Johnny' # alterando valor
# # sobrenome = aluno_djonny.get('sobrenome')

# print(nome)
# # print(sobrenome)
# print(aluno_djonny.keys())
# print(aluno_djonny.values())
# print(aluno_djonny.items())
# print(aluno_djonny)
# print(type(aluno_djonny)) #tipo dicionario
print(aluno_djonny)

# lista = [1,2,3]
# dicionario = {'chave': 'valor'}
# tupla = (1,2,3)

# print(lista)
# print(dicionario)
# print(tupla)

# lista[0] = 10
# tupla[0] = 10

# print(lista)
# print(tupla) # não sofre alteração

# dias_semana = ('Seg', 'Terc', 'Qua', 'Qui', 'Sex')
# usuario = [1,2,3,4,5]
# amigos = [(1,3), (1,4)]




