# ask preço de venda
# bid preço de compra

import requests, json

def apiDolar():

    url = "https://economia.awesomeapi.com.br/json/last/USD-BRL"


    dados = requests.get(url).content

    cotacao = json.loads(dados)

    valor = cotacao['USDBRL']['ask']

    return valor


