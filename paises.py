import json

import requests

URL_ALL = 'https://restcountries.com/v2/all'
URL_NAME = 'https://restcountries.com/v2/name'


def requisicao(url):
    try:
        resposta = requests.get(url)
        if resposta.status_code == 200:
            return resposta.text
    except:
        print(f'erro ao fazer requisição em {url}')


def parsing(resposta_requisicao):
    try:
        return json.loads(resposta_requisicao)
    except:
        print('Erro no parsing')


def contagem_paises(lista_de_paises):
    return len(lista_de_paises)


def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name'])


def mostrar_poluacao(pais):
    resposta = requisicao(f'{URL_NAME}/{pais}')
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print(f"{pais['name']}: {pais['population']}")
        else:
            print(f'{pais} Não existe')


def mostrar_moeda(pais):
    resposta = requisicao(f'{URL_NAME}/{pais}')
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print(f'--------- Moeda de {pais["name"]} ---------')
                moedas = pais['currencies']
                for moeda in moedas:
                    print(f'          {moeda["name"]} - {moeda["code"]}')
        else:
            print(f'{pais} Não existe')


if __name__ == '__main__':
    mostrar_moeda('b')

    '''
    texto_da_resposta = requisicao(URL_ALL)
        if texto_da_resposta:
            lista_de_paises = parsing(texto_da_resposta)
            if lista_de_paises:
                listar_paises(lista_de_paises)
    '''