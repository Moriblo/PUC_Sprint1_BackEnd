Estruturação do Projeto `Lista de Obras de Arte`
Aluno: Moacyr Ribeiro Blondet
Turma: Engenharia de Software
Sprint 1: MVP Full Stack Básico

## `Requisitos Gerais`

Este é o MVP referente à Sprint **Desenvolvimento Full Stack Básico** 

O objetivo é realizar as entregas de acordo com os seguintes requisitos:

### 1 - Para o back-end e banco de dados:
1.1 - API com, pelo menos, três rotas (por exemplo, “/cadastrar_produto”, “/buscar_produto” e “/deletar_produto”), sendo que, pelo menos, uma delas deve implementar o método Post (por exemplo, na rota de cadastro).
*** Esta API tem: Uma `rota /` para direcionamento ao swagger. Uma `rota /obras` para obter a lista de todos os registros existentes na base `via requisição GET`. Uma `rota /obra` para inserir um item na base via `requisição POST` e para deletar um item da base via `requisição DELETE`. ***

1.2 - Fazer uso de um banco de dados SQLite ou PostgreSQL com, pelo menos, uma tabela (por exemplo, tabela de usuários cadastrados).
*** Este projeto está utilizando o SQLite, com uma tabela "obra". Vide detalhes na Classe Obra em model.obra.py ***

1.3 - Documentação da API em Swagger.
*** Através do flask pela rota / com redirect para /openapi/swagger. ***

### 2 - Para o front-end:
2.1 - Desenvolvimento de uma SPA (single page application) criativa e interativa.
*** Página index.html, com a imagem de um dos maiores museus do mundo (Musée du Louvre), além dos campos que precisam ser preenchidos e o botão para adicionar os dados na base. O campo Link, contém o endereço para informações adicionais à respectiva obra. Uma vez sendo selecionado o conteúdo do campo Link, pode ser acessado pelo botão direito do mouse pelo browser. ***

2.2 - Que na tela sejam apresentados itens em listas (por exemplo, lista de usuários ou livros).
*** As obras cadastradas são apresentadas na tela em formato de lista. ***

2.3 - Que, ao longo do código, seja feita a chamada a todas as rotas implementadas pela API.
*** A exceção da chamada à rota que gera a documentação (/), todas as rotas são acessadas pelas respectivas chamadas pelo front. ***

### 3 - Quanto à organização dos códigos:
3.1 - Devem ser criados dois projetos separados: um para a API e outro para o front-end.
*** Estão separados os arquivos py, pyc e sqlite, além do requirements.txt como back. Os arquivos js, css, mp4 e html, foram separados como front. ***

3.2 - Em ambos os projetos, deve existir um arquivo README.md com todas as orientações para a execução do código.
*** Este arquivo readme.md está separado na parte back do projeto. O readme_front.hml foi  inserido na parte front do projeto. ***

### 4 - Sobre a entrega:
4.1 - Deverá haver um vídeo de, no máximo, três minutos, apresentando a captura de tela com (I) a execução da API, com a interação com as rotas (via Swagger), e (II) a execução do front-end, com a interação com a aplicação, mostrando em quais momentos cada rota da API é chamada.
4.2 - Também deverá ser disponibilizados os dois projetos em repositórios públicos do GitHub. A entrega compreenderá três URLs, um para cada repositório público do GitHub e um para seu vídeo.

## `Como executar a API`

### 1 - Libs python:
*** Todas as libs python necessárias estão listadas no `requirements.txt` e deverão estar instaladas. ***

### 2 - Do ambiente
*** Como não está previsto upload deste projeto em nenhum ambiente compartilado, é fortemente indicado o uso de ambientes virtuais do tipo [virtualenv](https://virtualenv.pypa.io/en/latest/installation.html). ***

### 3 - Comandos a executar

*** Este comando instala as dependências/bibliotecas, descritas no arquivo `requirements.txt`. ***
```
(env)$ pip install -r requirements.txt
```

*** Durante o desenvolvimento, foi identicada a necessidade das instalações adicionais: ***
```
(env)$ pip install -U flask-openapi3
(env)$ pip install -U flask-cors
(env)$ pip install -U pylance
```

*** Para executar a API basta executar: ***
```
(env)$ flask run --host 0.0.0.0 --port 5000
```

## `Execução do Front`
*** Abra o file:///C:/env/index.html no navegador para carregar a página do aplicativo. ***
