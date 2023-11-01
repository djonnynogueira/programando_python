# https://www.hashtagtreinamentos.com/introducao-ao-beautifulsoup-python?gad_source=1
# Cotação do Dólar em Tempo Real:

import requests
from bs4 import BeautifulSoup

link = 'https://www.google.com/search?q=cota%C3%A7%C3%A3o+dolar'

# user-agent, esta é a linha que diz qual a versão do navegador que estamos pedindo.
headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36"}

requisicao = requests.get(link, headers = headers)
# print(requisicao)
# print(requisicao.text)

site =  BeautifulSoup(requisicao.text, "html.parser")
# print(site.prettify())

titulo = site.find_all("title")
# print(titulo)

pesquisa = site.find_all("input")
# print(pesquisa[1])

# pesquisa2 = site.find("input", class_="gLFyf")
# print(pesquisa2)

cotacao_dolar = site.find("span", class_="SwHCTb")

print(f'Cotação do dólar hoje: {cotacao_dolar.get_text()}') # -> pega a informação em formato de texto (valor arredondado)

print(f'Cotação do dólar hoje: {cotacao_dolar["data-value"]}') # -> busca a cotação do site (valor com mais casas decimais)

input('Pressione qualquer tecla para sair...')


# Instalando o pyinstaller:         pip install pyinstaller or py -m pip install pyinstaller
# Criando o executável:             pyinstaller --onefile imc.py
# Arquivo salvo dentro da pasta "dist"