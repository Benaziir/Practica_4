import requests

url='https://api.coindesk.com/v1/bpi/currentprice.json'

#1conectarse al sitio
response=requests.get(url)

#nos brinda informacion en formato jason
response.json()

#2 Recupero la informacion como json
data=response.json()

#Recupero el valor tipo cambio
bitcoin_dolar=data['bpi']['USD']['rate_float'] #compra del bitcon dolares
#bitcoin_libra=data['bpi']['GBP']['rate_float'] compra del bitcon libra
#bitcoin_euro=data['bpi']['EUR']['rate_float']  compra del bitcon euro

def moneda():
    try:
        n=float(input('Introduce un numero de bitcoins : '))
        print(f'El costo actual de {n} bitcoins es: {bitcoin_dolar * n:,.4f}')

    except:
        print('Ha ocurrido un error, vuelva a introducir el numero')
        return moneda()

moneda() 