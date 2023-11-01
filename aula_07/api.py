import json, requests

# VIA CEP
# url = 'https://viacep.com.br/ws/74740120json/'
# resposta = requests.get(url)
# conteudo = json.loads(resposta.content)
# print(conteudo)

# CRUD API

# JULIO
# url_api = 'https://6541a06df0b8287df1fe9099.mockapi.io/usuarios/'

url_api = 'https://6541a08cf0b8287df1fe90f5.mockapi.io/usuarios/'

usuario = {
    'usuario': 'Djonny',
    'senha': 'Asd202223'
}

# CREATE
# resposta = requests.post(url_api, data = usuario)
# print(resposta.status_code)

# READ
resposta = requests.get(url_api)
# print(resposta)
conteudo_api = json.loads(resposta.content)
# print(conteudo_api)

#UPDATE
resposta = requests.put(f"{url_api}/8", data=usuario)
# print(resposta.status_code)

#DELETE
resposta = requests.delete(f"{url_api}/8")
# print(resposta.status_code)
