import requests
from PIL import Image
from translate import Translator
from io import BytesIO
import json
from dotenv import load_dotenv
import os

config = load_dotenv(".env")
languague = Translator(from_lang="en",to_lang='pt-br')
API_MOVIE_KEY = os.getenv('API_KEY')
movie_title = input('Informe um filme: ')
api_movie = f'http://www.omdbapi.com/?apikey={API_MOVIE_KEY}&t={movie_title}'

response = requests.get(api_movie)
data = json.loads(response.text)

title  = data['Title']
year = data['Year']
runtime = data['Runtime']
genre = data['Genre']
plot = data['Plot']
poster = data['Poster']
diretor = data['Director']

response_poster = requests.get(poster)
if 'image' in response_poster.headers['content-type']:
    open_img = Image.open(BytesIO(response_poster.content))
    open_img.save('poster.jpg')
    open_img.show()


else:
    print('A URL não contém uma imagem válida.')

try:
    resultado = languague.translate(plot)
except StopIteration:
    print('Não foi possível traduzir a sinopse do filme.')
    resultado = ''
except ValueError:
    print('A sinopse do filme é inválida.')
    resultado = ''
except Exception as e:
    print(f'Erro desconhecido: {str(e)}')
    resultado = ''

plot_traduzido = resultado
msg = f'Titulo: {title}\nAno de Lançamento: {year}\nGenero: {genre}\nSinopse: {plot_traduzido}'
print(msg)
