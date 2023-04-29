# Sist. GerenciamentoUser

Este código é uma aplicação web Flask que possui rotas para login, logout, página principal e cadastro de novos usuários.

Para executar o código use o arquivo `run.py`, dando play.

A estrutura de pastas da aplicação é a seguinte:

O arquivo __init__.py na pasta app/models define o modelo de dados utilizado pela aplicação, que neste caso possui apenas a entidade User com as seguintes informações: id, first_name, last_name, email, phone_number, password e gender.
O arquivo __init__.py na pasta app/routes define as rotas da aplicação:
A rota '/' é a página principal da aplicação, que só pode ser acessada por usuários logados.
A rota '/login' é utilizada para o usuário fazer o login. Caso o usuário já esteja logado, ele é redirecionado para a página principal. Caso contrário, é exibido o formulário de login. Caso o método da requisição seja POST, é verificado se o email do usuário está cadastrado. Se não estiver, é exibido uma mensagem de erro. Caso esteja, o usuário é logado e redirecionado para a página principal.
A rota '/logout' é utilizada para o usuário sair da aplicação. O usuário é deslogado e redirecionado para a página de login.
A rota '/register' é utilizada para o usuário criar uma nova conta. Caso o método da requisição seja POST, é verificado se a senha digitada é igual a de confirmação. Se for diferente, é exibida uma mensagem de erro. Caso contrário, é criado um novo usuário no banco de dados e o usuário é redirecionado para a página de cadastro com uma mensagem de sucesso. Caso o método da requisição seja GET, é exibido o formulário de cadastro.
O arquivo __init__.py na pasta app é o arquivo principal da aplicação e é responsável por inicializar a instância do Flask e o banco de dados. A instância do Flask é criada com o nome da aplicação e a configuração da conexão com o banco de dados. O banco de dados utilizado é o SQLite, que é criado na pasta da aplicação. A configuração da aplicação é carregada a partir de um arquivo de configuração externo. Além disso, são importadas as rotas definidas no arquivo app/routes/__init__.py e é feita a criação das tabelas no banco de dados, caso elas ainda não existam.

O arquivo config.py define as configurações da aplicação. Ele define a chave secreta utilizada para gerar tokens de autenticação e a URL do banco de dados.

O arquivo base.html é o template HTML principal para a aplicação, o qual é estendido por outros templates. Ele inclui links para dois arquivos CSS: base.css e mobile-styles.css. O primeiro contém os estilos básicos para a aplicação, enquanto o segundo contém estilos para dispositivos móveis.

Os estilos CSS definem a aparência visual da aplicação. A tag body define a família de fontes, imagem de fundo e tamanho. A classe container define um container com layout flex, cor de fundo preta e borda com raio de 10px. A classe logo define um container de logo com texto alinhado à esquerda e uma imagem que se redimensiona para se ajustar ao container. A classe menu define um container de menu alinhado à direita com uma lista de itens de menu que são links para diferentes páginas na aplicação. A classe form define um container de formulário com texto centralizado e um botão de envio verde.

Os modelos são usados pelo Flask para renderizar páginas HTML que são enviadas aos clientes em resposta a solicitações. Existem quatro modelos neste trecho de código:

- app/templates/home.html: Este modelo é usado para renderizar a página inicial da aplicação web. Ele inclui uma mensagem de boas-vindas ao usuário e um link para fazer logout.

- app/templates/index.html: Este modelo é usado para renderizar a página principal da aplicação web. Se o usuário estiver logado, exibe uma mensagem de boas-vindas e algumas informações sobre o aplicativo. Caso contrário, solicita que o usuário faça login ou registre-se.

- app/templates/login.html: Este modelo é usado para renderizar a página de login da aplicação web. Ele inclui um formulário para o usuário inserir seu e-mail e senha para fazer login e exibe uma mensagem de erro se a tentativa de login falhar.

- app/templates/register.html: Este modelo é usado para renderizar a página de registro da aplicação web. Ele inclui um formulário para o usuário inserir seu nome, sobrenome, e-mail, número de telefone, senha e gênero. Ele também exibe uma mensagem de erro se a tentativa de registro falhar.

## Data Base

Para configurar o banco de dados desta aplicação, siga as seguintes instruções:

Certifique-se de ter um banco de dados PostgreSQL instalado e configurado em sua máquina. Caso contrário, você pode instalar o PostgreSQL em sua máquina local ou usar um serviço de hospedagem de banco de dados.

Abra o arquivo "config.py" na raiz do projeto e altere as informações de configuração do banco de dados para as suas próprias. Você precisará alterar os valores de "user", "password", "host", "port" e "database" para refletir suas próprias configurações.

Execute o seguinte comando no terminal para criar a tabela "users" no banco de dados:

```python
$ python
>>> from app import db
>>> db.create_all()
```

Esse comando criará a tabela "users" no banco de dados especificado nas configurações.


Você pode agora usar a tabela "users" em sua aplicação Python. Você pode acessá-la usando o modelo "User", que está definido no arquivo "models.py". O modelo "User" tem os campos "id", "first_name", "last_name", "email", "phone_number", "password" e "gender". Você pode adicionar, atualizar e excluir usuários no banco de dados usando as funções do modelo "User".

- Caso queira criar manualmente:

```sql
CREATE TABLE users (
  id SERIAL PRIMARY KEY,
  first_name VARCHAR(50) NOT NULL,
  last_name VARCHAR(50) NOT NULL,
  email VARCHAR(30) UNIQUE NOT NULL,
  phone_number VARCHAR(20) NOT NULL,
  password VARCHAR(30) NOT NULL,
  gender CHAR(1) NOT NULL
);
```
- SGBD usado: PostgreSQL

## Configurações

É recomendado criar um ambiente virtual para não fazer instalações desnecessárias, isso é possível da seguinte maneira:

- Abra o terminal do seu sistema operacional e navegue até o diretório onde deseja criar o ambiente virtual.

- Digite o seguinte comando para criar um novo ambiente virtual com o nome "venv":

```python -m venv venv```

- Se você estiver usando Python 3.x, pode precisar usar o comando "python3" em vez de "python".

- Aguarde até que o ambiente virtual seja criado.

Também em `config.py`, configure sua senha, nome do banco de dados, caso tenha usado um outro nome e a porta, caso queira alterar a porta. Segue abaixo os campos de alteração:

```python
DATABASE = 'infosuser'
PORTA = '5432'
SENHA = '<sua_senha_aqui>'

DEBUG = True
SQLALCHEMY_TRACK_MODIFICATIONS = False
SECRET_KEY = "jdshbfkjsdbjdfjkghjsd"
SQLALCHEMY_DATABASE_URI = f"postgresql://postgres:{SENHA}@localhost:{PORTA}/{DATABASE}"
```