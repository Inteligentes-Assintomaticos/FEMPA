# TRIO DEVS — ATV09

> **Integrantes:** Felipe Gabriel Araújo de Freitas | Matheus Ramos Lima da Silva | Paulo Lázaro da Rocha Souza

## Sobre o projeto

O TRIO DEVS é um portal desenvolvido originalmente com HTML, CSS e JavaScript na ATV06 e integrado ao Django na ATV09. O projeto mantém a identidade visual do site original e permite administrar os conteúdos e itens de navegação pelo Django Admin.

Os conteúdos são armazenados no modelo `Conteudo`, e os links do menu no modelo `Menu`. A navegação interna é feita pelas URLs do Django; os links externos usam as URLs cadastradas no Admin.

## Funcionalidades

- Página inicial e páginas internas carregadas do banco de dados.
- Menu dinâmico, ordenável e administrável.
- Cadastro, edição, ativação e remoção de conteúdos e itens de menu pelo Django Admin.
- CSS e imagens organizados como arquivos estáticos da aplicação.

## Tecnologias

- Python 3.14
- Django 6.1.2
- HTML5 e CSS3
- SQLite

## Estrutura do projeto

```text
ATV09_FELIPE_MATHEUS_PAULO/
├── django/
│   ├── config/             # Configurações e URLs do projeto Django
│   ├── portal/             # Models, Views, Admin e URLs da aplicação
│   │   ├── migrations/     # Migrações do banco de dados
│   │   ├── static/         # CSS e imagens
│   │   └── templates/      # Templates Django
│   ├── db.sqlite3          # Banco SQLite com os conteúdos cadastrados
│   └── manage.py
├── requirements.txt        # Dependências Python do projeto
└── README.md
```

## Como executar

Os comandos abaixo partem da pasta raiz do projeto, onde estão `requirements.txt` e a pasta `django`.

### 1. Criar e ativar o ambiente virtual

Linux/macOS:

```bash
python3 -m venv .venv
source .venv/bin/activate
```

Windows PowerShell:

```powershell
py -m venv .venv
.venv\Scripts\Activate.ps1
```

### 2. Instalar as dependências

```bash
python -m pip install -r requirements.txt
```

### 3. Aplicar as migrações

```bash
cd django
python manage.py migrate
```

### 4. Acessar ou criar um usuário administrador

O banco `django/db.sqlite3` incluído na entrega já possui um superusuário para acesso local ao Django Admin:

- Usuário: `admin`
- Senha: `admin`

Essas são credenciais de demonstração para avaliação local. Se preferir criar outra conta administradora, execute a partir da pasta `django`:

```bash
python manage.py createsuperuser
```

Siga as instruções do terminal para informar nome de usuário, e-mail e senha. Escolha um nome diferente de `admin`, pois esse usuário já existe no banco incluído.

### 5. Iniciar o servidor

```bash
python manage.py runserver
```

## Acessos

- Portal: <http://127.0.0.1:8000/>
- Django Admin: <http://127.0.0.1:8000/admin/>

## Repositório

<https://github.com/Inteligentes-Assintomaticos/FEMPA/tree/ATV09>
