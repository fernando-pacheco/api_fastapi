import requests
from pprint import pprint
import json

url = 'https://guilhermeonrails.github.io/api-restaurantes/restaurantes.json'

response = requests.get(url)

if response.status_code == 200:
    dados_json = response.json()
    dados_restaurantes = {}
    for item in dados_json:
        nome_restaurante = item['Company']
        if nome_restaurante not in dados_restaurantes:
            dados_restaurantes[nome_restaurante] = []

        dados_restaurantes[nome_restaurante].append({
            'item': item['Item'],
            'preco': item['price'],
            'descricao': item['description']
        })
else:
    print(response.status_code)

for nome_restaurante, dados in dados_restaurantes.items():
    nome_arquivo = f'{nome_restaurante}.json'
    with open(nome_arquivo,'w') as arquivo:
        json.dump(dados, arquivo, indent=4)