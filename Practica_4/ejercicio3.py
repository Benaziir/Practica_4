import random
from pyfiglet import Figlet
figlet = Figlet()
fuentes=figlet.getFonts()
#Ejemplos de fuentes:'alligator', 'alligator2', 'alphabet', 'aquaplan', 'arrows'

def fuente_texto():
    fuente=input('Ingrese una fuente: ')
    texto=input('Ingrese un texto: ')
    if fuente in fuentes:
        figlet.setFont(font=fuente)
        print(figlet.renderText(texto))
        print(f'Fuente utilizada: {fuente}\n')
    else:
        print(f'Error, la fuente "{fuente}" no existe.\n')
        fuente=random.choice(fuentes)
        figlet.setFont(font=fuente)
        print(figlet.renderText(texto))
        print(f'Fuente utilizada: {fuente}')
fuente_texto()