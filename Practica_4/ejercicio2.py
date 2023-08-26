"""
Obtener una imagen situada en el siguiente sitio web.

https://unsplash.com/es/s/fotos/perrito
"""
import requests


url = 'https://unsplash.com/es/fotos/9LkqymZFLrE'

response = requests.get(url)

with open('perrinho.jpg', 'wb') as f:
    f.write(response.content)
    pass