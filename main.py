import requests
from PIL import Image, ImageTk
from translate import Translator
from io import BytesIO
import tkinter as tk


'''
Proximos passos: 
Criar GUI
Traduzir nome do filme de en para pt-br

'''
translator = Translator(from_lang="en", to_lang='pt-br')

def movieSearch():
    movie_title = entry.get()
    api_movie = f'http://www.omdbapi.com/?apikey=30c395bf&t={movie_title}'
    
    response = requests.get(api_movie)
    data = response.json()
    
    title = data['Title']
    year = data['Year']
    genre = data['Genre']
    plot = data['Plot']
    poster = data['Poster']
    
    response_poster = requests.get(poster)
    if 'image' in response_poster.headers['content-type']:
        img = Image.open(BytesIO(response_poster.content))
        img.save('poster.jpg')
        imagem = ImageTk.PhotoImage(img)
        image_label.config(image=imagem)
        image_label.image = imagem
    else:
        print('A URL não contém uma imagem válida.')
        image_label.config(image=None)
        image_label.image = None
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
    msg = f'Titulo: {title}\nAno de Lançamento: {year}\nGenero: {genre}\nSinopse: {translated_plot}'
    result.config(text=msg)

janela = tk.Tk()
janela.title('Info Movie')

font = ('Arial', 14)

entry = tk.Entry(janela)
entry.pack()

entry.bind("<Return>", lambda x: movieSearch())

search = tk.Button(janela, text='Pesquisar Filme', command=movieSearch)
search.pack()

result = tk.Label(janela, text=None, wraplength=500, font=font)
result.pack()

image_label = tk.Label(janela, image='')
image_label.pack()

janela.mainloop()






