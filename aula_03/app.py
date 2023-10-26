# PROCEDURAL
a = 10
b = 100

# print(a+b)

# # FUNÇÃO SOMAR
# def somar_sem_retorno():
#     print("Realizando a soma...")
#     print(a+b)

# # retorna
# def somar_retorna():
#     return a+b


# resultado = somar_retorna()
# print (resultado)

## Com parametro
# def somar_com_param(a, b):
#     print(a+b)
    
# somar_com_param(2, 9)

## Com parametro padrão
def somar_com_param_padrao(a=10, b=10):
    print(a+b)
    
somar_com_param_padrao(13)