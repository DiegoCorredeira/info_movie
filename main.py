import requests
from PIL import Image
from translate import Translator
from io import BytesIO
import json
from dotenv import load_dotenv
import os

load_dotenv(".env")
translator = Translator(from_lang="en", to_lang='pt-br')
movie_title = input('Informe um filme: ')
api_movie = f'http://www.omdbapi.com/?apikey=30c395bf&t={movie_title}'

response = requests.get(api_movie)
data = response.json()

title = data['Title']
year = data['Year']
runtime = data['Runtime']
genre = data['Genre']
plot = data['Plot']
poster = data['Poster']
director = data['Director']

response_poster = requests.get(poster)
if 'image' in response_poster.headers['content-type']:
    img = Image.open(BytesIO(response_poster.content))
    img.save('poster.jpg')
    img.show()
else:
    print('A URL não contém uma imagem válida.')

try:
    translated_plot = translator.translate(plot)
except StopIteration:
    print('Não foi possível traduzir a sinopse do filme.')
    translated_plot = ''
except ValueError:
    print('A sinopse do filme é inválida.')
    translated_plot = ''
except Exception as e:
    print(f'Erro desconhecido: {str(e)}')
    resultado = ''

plot_traduzido = resultado
msg = f'Titulo: {title}\nAno de Lançamento: {year}\nGenero: {genre}\nSinopse: {plot_traduzido}'
print(msg)
