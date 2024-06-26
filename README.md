

# Django App Docker Base <a href="https://opensource.org/license/mit"><img src='https://img.shields.io/badge/license-MIT-blue'></a><a href="https://www.python.org/downloads/release/python-3122/"> <img src='https://img.shields.io/badge/python-3.12.2-blue?logo=python'></a><br> (Celery e Selenium incluídos)

Este repositório serve como uma base para a construção de aplicações Django, Celery e Selenium em contêineres Docker. Ele fornece uma estrutura inicial e configuração básica para você começar a desenvolver seu aplicativo Django em um ambiente de contêiner.

## 1. Pré-requisitos

Certifique-se de ter o Docker instalado em sua máquina antes de prosseguir. Você pode encontrar instruções de instalação no site oficial do Docker: [Docker Installation Guide](https://docs.docker.com/get-docker/).

## 2. Como usar este repositório

1. Clone este repositório para o seu ambiente de desenvolvimento local:

```bash
git clone https://github.com/caiython/djangoapp-docker-base.git
```

2. No diretório `dotenv_files`, renomeie o arquivo `.env-example` para `.env`.

3. Abra o arquivo renomeado `.env` com um editor de texto e edite as variáveis de ambiente para corresponder ao seu.

4. Dentro da raíz do repositório, execute o comando para construir o contêiner Docker:

```bash
docker compose up --build
```

5. Teste a aplicação acessando o endereço `http://127.0.0.1:8000` ou `http://localhost:8000` no seu navegador. Se tudo ocorreu bem, a página deverá exibir um `Hello World` em `JsonResponse`.

6. Se você chegou até aqui, basta começar a desenvolver a sua própria aplicação.

> *Caso ocorra algum erro, você pode checar a seção **5. Problemas Conhecidos***

## 3. Estrutura do Projeto

A estrutura do projeto é a seguinte:

```
djangoapp-docker-base/
│
├── .dockerignore
├── .gitignore
├── docker-compose.yml
├── Dockerfile
├── LICENSE
├── README.md
├── .vscode/
│   └── settings.json
├── djangoapp/
│   ├── manage.py
│   ├── requirements.txt
│   ├── app/
│   │   ├── __init__.py
│   │   ├── admin.py
│   │   ├── apps.py
│   │   ├── models.py
│   │   ├── tasks.py
│   │   ├── tests.py
│   │   ├── urls.py
│   │   ├── views.py
│   │   └── migrations/
│   │       └── __init__.py
│   └── project/
│       ├── __init__.py
│       ├── asgi.py
│       ├── celery.py
│       ├── settings.py
│       ├── urls.py
│       └── wsgi.py
├── dotenv_files/
│   └── .env-example
└── scripts/
    └── commands.sh
```

## 4. Comandos Úteis
Aqui estão alguns comandos úteis que você pode usar durante o desenvolvimento do seu aplicativo Django dentro do contêiner Docker.

### Executar o Servidor de Desenvolvimento
```bash
docker-compose up
```
Este comando inicia o servidor de desenvolvimento e expõe o aplicativo.

### Criar App Django
```bash
docker-compose run djangoapp python manage.py startapp meu_app
```
Este comando cria um app no seu projeto com o nome `meu_app`.

### Executar Migrações do Django
```bash
docker-compose run djangoapp python manage.py migrate
```
Este comando executa as migrações do Django no banco de dados.

### Criar Superusuário
```bash
docker-compose run djangoapp python manage.py createsuperuser
```
Este comando cria um superusuário para acessar o painel de administração do Django.

### Atualizar Dependências
```bash
docker-compose run djangoapp pip install -r requirements.txt
```
Este comando atualiza as dependências Python do seu aplicativo com base no arquivo `requirements.txt`.

### Acessar o Shell
```bash
docker-compose run djangoapp python manage.py shell
```
Este comando abre o shell Python interativo do Django para interagir com o seu aplicativo.

## 5. Problemas Conhecidos

Abaixo listarei alguns problemas conhecidos que você pode acabar se deparando ao tentar rodar o repositório na sua máquina.

### DjangoApp Finalizando ao Executar o Arquivo `commands.sh`

Caso o container do seu djangoapp esteja encerrando com a mensagem abaixo, provavelmente é um erro de caracteres do Windows (CR LF)

```bash
djangoapp | exec /scripts/commands.sh: no such file or directory
djangoapp exited with code 1
```

Para solucionar este problema você deve seguir os seguintes passos:

1. Baixe e instale na sua máquina o software editor de texto `Notepad++`

2. Navegue até o diretório `scripts` e abra o arquivo `commands.sh` com o `Notepad++`

3. Com o arquivo aberto no editor de texto, localize a barra de menu no topo do aplicativo, clique sobre `Edit`, clique na opção `EOL Conversion`, e então selecione `Unix (LF)`

4. Salve o arquivo e o reconstrua o container através dos comandos `docker-compose down` e `docker-compose up --build`

### DjangoApp Não se Conecta ao PostgreSQL

Este problema pode aparecer dependendo do seu sistema operacional. O DjangoApp não inicia pois fica aguardando a inicialização do banco eternamente, apresentando um destes dois casos nas linhas no terminal:

- localhost 5432
```bash
...
djangoapp     | 🟡 Waiting for Postgres Database Startup (localhost 5432)
djangoapp     | 🟡 Waiting for Postgres Database Startup (localhost 5432)
djangoapp     | 🟡 Waiting for Postgres Database Startup (localhost 5432)
...
```
- psql 5432
```bash
...
djangoapp     | 🟡 Waiting for Postgres Database Startup (psql 5432)
djangoapp     | 🟡 Waiting for Postgres Database Startup (psql 5432)
djangoapp     | 🟡 Waiting for Postgres Database Startup (psql 5432)
...
```

Acontece que o banco inicializa normalmente mas o DjangoApp não o localiza através do endereço definido no dotenv. Para corrigir este erro você pode realizar a seguinte mudança:

1. Navegue até o diretório `.dotenv_files` e abra o seu arquivo `.env` com um editor de texto

2. Aqui teremos dois casos, vou descrever os dois para que você teste, pois o resultado dependerá do seu sistema operacional. Você deverá alterar o valor da variável de ambiente `POSTGRES_HOST`

    - Caso o valor esteja `localhost`, altere para `psql` (nome do contêiner postgresql)

    - Caso o valor esteja `psql` (nome do contêiner postgresql), altere para `localhost`

3. Salve o arquivo e o reconstrua o container através dos comandos `docker-compose down` e `docker-compose up --build`. Isso deverá resolver o problema.

## 6. Contribuições

Se você encontrar problemas ou tiver sugestões de melhorias, sinta-se à vontade para abrir uma issue neste repositório. Estarei feliz em receber contribuições!

## 7. Agradecimentos Especiais

- Roberto Júnior (@betobraga)
- Fábio Solidade
- Carlos Alberto / Catec Tester

Obrigado pelo apoio durante o desenvolvimento do projeto. Vocês são feras!

## 8. Baseado no Conteúdo de Otávio Miranda

Este repositório foi construído com base no conteúdo disponibilizado pelo Otávio Miranda no vídeo [Docker com Django, PostgreSQL e Compose para seu ambiente de desenvolvimento Python](https://docs.docker.com/get-docker/).

## 9. Licença

Este projeto está licenciado sob a [MIT License](https://opensource.org/license/mit).