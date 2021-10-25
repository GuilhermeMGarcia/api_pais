import json
import sys

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


def contagem_paises():
    resposta = requisicao(URL_ALL)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            return len(lista_de_paises)


def listar_paises(lista_de_paises):
    for pais in lista_de_paises:
        print(pais['name'])


def mostrar_poluacao(pais=None):
    if pais is None:
        url = URL_ALL
    else:
        url = f'{URL_NAME}/{pais}'
    resposta = requisicao(url)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print(f"{pais['name']}: {pais['population']}")
        else:
            print(f'{pais} Não existe')


def mostrar_moeda(pais=None):
    if pais is None:
        url = URL_ALL
    else:
        url = f'{URL_NAME}/{pais}'
    resposta = requisicao(url)
    if resposta:
        lista_de_paises = parsing(resposta)
        if lista_de_paises:
            for pais in lista_de_paises:
                print(f'--------- Moeda de {pais["name"]} ---------')
                try:
                    moedas = pais['currencies']
                    for moeda in moedas:
                        print(f'          {moeda["name"]} - {moeda["code"]}')
                except:
                    print(f'Error')
        else:
            print(f'{pais} Não existe')


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print('## Bem vindo ao sistema de paises ##')
        print('Uso: python paises.py <acao> <nome do pais>')
        print('Ações disponiveis: contagem, populacao, moeda')
    else:
        argumento1 = sys.argv[1]
        if argumento1 == 'contagem':
            numero_de_paises = contagem_paises()
            print(f'Contem {numero_de_paises} no mundo.')
        elif argumento1 == 'populacao':
            try:
                argumento2 = sys.argv[2]
                mostrar_poluacao(argumento2)
            except:
                argumento2 = None
                mostrar_poluacao(argumento2)
        elif argumento1 == 'moeda':
            try:
                argumento2 = sys.argv[2]
                mostrar_moeda(argumento2)
            except:
                argumento2 = None
                mostrar_moeda(argumento2)
