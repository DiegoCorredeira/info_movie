# Descrição

Este código utiliza a API do OMDb para recuperar informações sobre um filme especificado pelo usuário, incluindo título, ano de lançamento, gênero, sinopse e pôster. Ele também utiliza a biblioteca translate para traduzir a sinopse do filme do inglês para o português brasileiro.
Pré-requisitos

### Antes de executar este código, certifique-se de ter as seguintes bibliotecas instaladas:

    requests
    PIL
    translate
    json

##### Você também precisa se inscrever na API do OMDb e obter uma chave de API válida. Você pode fazer isso em http://www.omdbapi.com/.
## Como usar

    Certifique-se de que todas as bibliotecas necessárias foram instaladas e a chave de API do OMDb foi obtida.
    Crie um arquivo .env na mesma pasta onde está o seu script Python e defina a variável API_KEY com a sua chave de API do OMDb.
    Execute o script Python e insira o título do filme que você deseja procurar.
    O script irá recuperar as informações do filme da API do OMDb e tentar traduzir a sinopse do filme para o português brasileiro.
    Se a API do OMDb retornar uma URL de imagem para o pôster do filme, o script irá tentar baixar e salvar o pôster como um arquivo "poster.jpg" na mesma pasta onde está o seu script Python.
    O script exibe as informações do filme, incluindo o título, ano de lançamento, gênero e sinopse traduzida (se disponível).

Limitações

## Este código tem as seguintes limitações:

    Ele só é capaz de recuperar informações sobre um único filme por vez.
    A tradução da sinopse pode não ser 100% precisa e depende da qualidade da tradução fornecida pela API do translate.
    O código não faz nenhuma validação de entrada do usuário, portanto, se o usuário inserir um título de filme inválido ou não fornecer entrada, o código pode falhar.
