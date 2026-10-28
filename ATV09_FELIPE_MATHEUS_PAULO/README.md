# ATV09 - Portal Trio Devs em Django

**Integrantes:** Felipe Gabriel Araújo de Freitas, Matheus Ramos Lima da Silva e Paulo Lázaro da Rocha Souza (ATV06 - turma 523).

## Sobre o projeto

Evolução do portal da ATV06 para Django. A identidade visual, o CSS responsivo e as imagens foram reaproveitados. Os conteúdos e itens de navegação são registros editáveis no Django Admin; a navegação interna usa URLs por slug.

## Tecnologias

- Python 3.10 ou superior
- Django 5.2
- SQLite
- HTML semântico e CSS responsivo

## Instalação e execução

No terminal, a partir desta pasta:

```powershell
python -m venv .venv
& .\.venv\Scripts\Activate.ps1
python -m pip install -r requirements.txt
python manage.py migrate
python manage.py loaddata portal/fixtures/initial_portal.json
python manage.py createsuperuser
python manage.py runserver
```

Abra a aplicação em <http://127.0.0.1:8000/> e o Django Admin em <http://127.0.0.1:8000/admin/>.

O fixture inicial carrega a página inicial, seis páginas internas (currículos e temas dos integrantes) e dois links externos. Para restaurar esse conjunto em um banco vazio, execute `loaddata` novamente. Os arquivos CSS e as imagens ficam em `portal/static/portal/`.

## Estrutura

- `config/`: configurações e URLs do projeto Django.
- `portal/`: Models, Views, Admin, Template, migration e arquivos estáticos.
- `portal/fixtures/initial_portal.json`: conteúdo e menu de demonstração.
- `db.sqlite3`: criado localmente ao aplicar as migrations; não é versionado.

O campo HTML do Admin deve conter apenas o conteúdo interno da página. A estrutura do documento, cabeçalho, navegação e rodapé ficam no Template base.
