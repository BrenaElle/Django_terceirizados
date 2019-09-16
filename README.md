# Django_terceirizados

## Proposta


### Pré-requesitos
* **Python3.7 >**

### Instalação

É necessario que você possua em seu computador uma pasta com um `virtualenv` ativo em algum diretório do seu computador, caso não tenha, siga os passos a seguir:

```sh
$ py -m venv env
$ .\env\bin\activate
```

Primeiramente, tenha certeza de estar utilizando a versão mais recente do **Python** será preciso ter todos os arquivos necessários em seu computador, para isso copie o link do projeto e depois execute o comando `git clone` no terminal, assim o programa será instalado em sua máquina.

```sh
$ git clone https://github.com/BrenaElle/Django_terceirizados.git
```

Depois de terminar esta etapa, é preciso que o executar a instalação das bibliotecas necessárias para rodar o projeto `requirements.txt` .Execute o seguinte comando:

```sh
(venv)$$ py -m pip install -r requirements.txt
```

Or

```sh
(venv)$ py -m pip install -r requirements.txt
```

### DataBase

Com tudo isso instalado, é hora de configurar a conexão com o banco de dados.Na pasta `/terceirizados/settings` estão as configurações do banco de dados que podem ser alteradas ou utilizadas para a criação de um banco de dados com o sqlite3. 

```python
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}
```

### Migrations

Com todos os passos anteriores feitos com sucesso, agora será preciso aplicar o comando `makemigrations` e `migrate`.

```sh
(venv)$ cd 'path_to_project'/Django_terceirizados
(venv)$ py manage.py makemigrations core
(venv)$ py manage.py makemigrations services
(venv)$ py manage.py migrate
```

### Criando um administrador

Para ter acesso às ferramentas de administrador do sistema, é preciso criar uma conta como `superuser`, assim como mostra o exemplo:

```sh
(venv)$ py manage.py createsuperuser
```


### Iniciando o servidor

Por fim, o que será acertado a se fazer é iniciar o funcionamento do servidor com o comando `runserver`.

```sh
(venv)$ cd django_terceirizados
(venv)$ py manage.py runserver
```

## Desenvolvido com

* [Python](https://www.python.org) - Linguagem de programação
* [Django](https://www.djangoproject.com) - O web framework utilizado

## Autores

* **Brena Ellen Feitoza Marques**
