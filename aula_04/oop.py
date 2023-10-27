#OOP

# ABSTRAÇÃO, OBJETO, ATRIBUTOS, METHODOS

# CLASSE (Abrastração)

class Carro:
    def __init__(self, cor, modelo, fabricante):
        self.cor = cor
        self.modelo = modelo
        self.fabricante = fabricante

# Objeto
# carro_red = Carro("Red")
# carro_blue = Carro("Blue")
# carro_green = Carro("Green")
   
carro_green = Carro("Green","Gol","VOlkswagem")
carro_white = Carro("White","F10","Ford")
carro_red = Carro("Red","Uno","Fiat")
   
# Atributo
# print(carro_red)
# print(Carro())

# print(carro_red.cor)
# print(carro_blue.cor)
# print(carro_green.cor)

print(carro_green.cor)
print(carro_green.modelo)
print(carro_green.fabricante)

# print(carro_red.minhacor)