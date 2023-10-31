peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))
imc = peso / (altura * altura)
print('='*25)
print(f'Seu IMC é de {imc:.2f}.')
print('='*25)
input('Pressione qualquer telcla para sair...')

# Instalando o pyinstaller:         pip install pyinstaller
# Criando o executável:             pyinstaller --onefile imc.py
# Arquivo salvo dentro da pasta "dist"