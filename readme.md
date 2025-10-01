# Projeto Django - Blog de Notícias

Este projeto é um blog simples em Django, onde usuários podem criar, visualizar, editar e excluir notícias.

---

## Pré-requisitos

- Python 3.10+  
- pip  
- Virtualenv (opcional, mas recomendado)  
- SQLite (já vem com Python) ou outro banco de dados configurado

---

## Passos para rodar o projeto

1. **Clonar o repositório**

```bash
git clone <URL_DO_REPOSITORIO>
cd <NOME_DO_PROJETO>
```
## Criar e ativar ambiente virtual (opcional)
python -m venv venv
# Windows
venv\Scripts\activate
# macOS/Linux
source venv/bin/activate

## Instalar dependencias
pip install -r requirements.txt

## Criar as tabelas do banco de dados
python manage.py makemigrations
python manage.py migrate

## Rodar o servidor
python manage.py runserver
