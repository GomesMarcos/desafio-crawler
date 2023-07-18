# Desafio Crawler:

## Intro
Fui desafiado a criar um projeto de raspagem de dados.
Por gostar de filmes e ser uma página gerada por JS, o que aumenta o nível de complexidade, escolhi a opção: [imdb.com](https://www.imdb.com/chart/top/?ref_=nv_mv_250)

### Dependências:

- Local: 
  - Python 3.11
  - venv / virtualenv / etc.
  - Navegador Firefox
  - Ter um prova da consulta (Screenshot)
- Conteinerizado:
  - docker
  - docker-compose

### Instalação:
- Local:
  - `$ python3 -m venv venv`
  - `$ source venv/bin/activate`
  - `$ pip install -r requirements.txt`
    - `$ pip install -r requirements-dev.txt` (opcional: caso queira instalar as dependências de desenvolvimento utilizadas neste projeto)
<br>
- Containerizado:
  - `$ docker-compose up -d`

### Execução do projeto:
- Local:
  - Certifiqe-se de que a venv está ativa `$ source venv/bin/activate`
  - `$ python app.py`

- Containerizado:
  - Certifiqe-se de que os containeres estão rodando `$ docker-compose up -d`
 - `$ docker exec -it desafio-crawler-app-1 bash`
 - `# python app.py`

### Arquivos gerados na execução:
- db.sqlite3 -> armazena os dados em banco relacional
- movies.json -> armazena os dados em arquivo .json
- screenshot.b64 -> screenshot no formato <i> base64</i> dos filmes.
- movies.png -> screenshot dos filmes a partir da execução `$ python convert_to_png.py`.


