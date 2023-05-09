import requests
import json
import textwrap
from PIL import Image, ImageTk
from translate import Translator
from io import BytesIO
import tkinter as tk
from ttkthemes import ThemedTk
from dotenv import load_dotenv
import os

# > Banco de dados dos pesquisados
# > Talvez permitir busca por nome nacional
translator = Translator(from_lang="en", to_lang='pt-br')

def movieSearch():
    movie_title = entry.get()
    api_movie = f'http://www.omdbapi.com/?apikey=30c395bf&t={movie_title}'
    response = requests.get(api_movie)
    data = response.json()
    
    if data['Response'] == 'False':
         result.config(text='Informe um título valido', fg='red', font=font)
         entry.delete(0, tk.END)
         return
    
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
        wrapped_plot = textwrap.fill(translated_plot, width=60)
    except Exception as e:
        print(f'Erro desconhecido: {str(e)}')
        wrapped_plot = ''
        
    msg = f'Titulo: {title}\nAno de Lançamento: {year}\nGenero: {genre}\nSinopse: {wrapped_plot}'
    result.config(text=msg, fg='black')
    entry.delete(0, tk.END)

    saveMovie(title, year, genre, translated_plot)

def saveMovie(title, year, genre, translated_plot):
    data_movie = {
        'title' : title,
        'year' : year,
        'genre' : genre,
        'plot' : translated_plot,
        
    }
    with open('salvar_filmes.txt', 'a', encoding='UTF-8') as arquivo:
        arquivo.write(json.dumps(data_movie) + '\n \n')
    

root = tk.Tk()
root.title('DB Movie')
font = ('Arial', 14)

entry = tk.Entry(root, font=font)
entry.pack(padx=15, pady=15, side=tk.LEFT)

entry.bind("<Return>", lambda x: movieSearch())

search = tk.Button(root, text='Pesquisar Filme', command=movieSearch)
search.pack(padx=15, pady=15, side=tk.LEFT)


image_label = tk.Label(root)
image_label.pack(padx=10, pady=10, side=tk.RIGHT)


result = tk.Label(root, font=font, justify='left', anchor='w', wraplength=500)
result.config(fg='black')
result.pack(padx=10, pady=10, side=tk.RIGHT)


root.mainloop()






