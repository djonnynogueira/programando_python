import os

requirements = 'requirements.txt'
pasta = ' ../aula_05'
# pasta = r'..\aula_05'

# print(os.path.exists(f"{pasta}/{requirements}"))
# print(os.path.exists("../aula_05/requirements.txt"))

# res = os.path.exists("../aula_05/requirements.txt")

# if res:
#     print("Existe o arquivo!!")
# else:
#     print("Arquivo faltando")
    
    
# print(os.path.isfile("../aula_05/requirements.txt")) #verifica se é arquivo
# print(os.path.isdir("../aula_05")) #verifica se é pasta

# print(os.getcwd()) # onde está
# print(os.chdir('../aula_05')) # caminha até o local informado
# print(os.getcwd()) # onde está, após alteração de lugar

# raiz = 'c:/python'

# if os.getcwd() == raiz: os.chdir(raiz)
    
# print(os.getcwd())

# # print(os.mkdir('../aula_05/manutencoes'))  #cria pasta
# # print(os.mkdir('manutencoes'))  #cria pasta
# # print(os.rmdir('manutencoes'))  #excluir pasta

# print(os.listdir('../aula_05'))  #excluir pasta

# aq = 0
# pastas = 0

# for info in os.listdir('../aula_05'):
#     if os.path.isfile(f'../aula_05/{info}'):
#         aq += 1
#     else:
#         pastas += 1
        
# print(f'Tem {aq} arquivos e {pastas} pastas.')

# os.system('rmdir djonny') # executa comandos do terminal
# os.system('mkdir djonny') # executa comandos do terminal

os.system('type null > file.txt') # executa comandos do terminal
# os.system('del file.txt') # executa comandos do terminal
# os.system('touch file.txt') # executa comandos do terminal

