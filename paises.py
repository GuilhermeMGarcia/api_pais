import json

import requests

URL_ALL = 'https://restcountries.com/v2/all'
URL_NAME = 'https://restcountries.com/v2/name/{name}'

resposta = requests.get(URL_ALL)

paises = json.loads(resposta.text) #parsing


for pais in paises:
    print(pais['name'])

