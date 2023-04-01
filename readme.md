# Info Movie

Este é um programa Python que utiliza a API do OMDB para buscar informações sobre filmes e exibir em uma interface gráfica simples. Ele também salva as informações do filme pesquisado em um arquivo de texto.

# Pré-requisitos

### Para executar o programa, é necessário ter o Python instalado, além dos seguintes pacotes Python:

    requests
    json
    textwrap
    Pillow (PIL)
    translate
    dotenv

##### Além disso, é necessário obter uma chave de API do OMDB.
## Instalação

    Clone o repositório ou baixe o arquivo info_movie.py.
    Instale as dependências do programa com o comando pip install -r requirements.txt.
    Crie um arquivo .env na mesma pasta do arquivo info_movie.py e insira sua chave de API do OMDB no formato API_KEY=chave_de_api.

## Como usar

Para executar o programa, abra o terminal na pasta onde o arquivo info_movie.py está localizado e execute o comando python info_movie.py.

Uma janela com a interface gráfica será aberta. Digite o nome do filme que deseja pesquisar no campo de texto e pressione Enter ou clique no botão "Pesquisar Filme". As informações sobre o filme serão exibidas na tela, incluindo o título, ano de lançamento, gênero e sinopse.

As informações do filme pesquisado também serão salvas em um arquivo de texto chamado salvar_filmes.txt, localizado na mesma pasta do arquivo info_movie.py.

## Imagens da interface gráfica

Interface primária:
![Interface Primária](https://i.imgur.com/dn62uGK.png)
Interface após a pesquisa pelo filme ser concluída:
![Interface Pesquisa](https://i.imgur.com/lWT1ubh.png)