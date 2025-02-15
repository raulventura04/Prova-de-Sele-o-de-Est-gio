# FastAPI, Pydantic e SQLAlchemy - API com Alembic

## Descrição
Este projeto é uma API desenvolvida com FastAPI, utilizando Pydantic para validação de dados e SQLAlchemy para interação com o banco de dados PostgreSQL. O Alembic é utilizado para controle de migrações do banco de dados.

## Tecnologias Utilizadas
- **FastAPI** - Framework web para APIs rápidas e eficientes
- **Pydantic** - Validação de dados
- **SQLAlchemy** - ORM para interação com banco de dados
- **Alembic** - Gerenciamento de migrações do banco de dados
- **PostgreSQL** - Banco de dados relacional
- **Python-dotenv** - Gerenciamento de variáveis de ambiente

## Instalação e Configuração
1. Clone este repositório:
   ```sh
   git clone https://github.com/{usuario}/{repositorio}.git
   cd {repositorio}
   ```

2. Crie e ative um ambiente virtual:
   ```sh
   python -m venv venv
   source venv/bin/activate  # Linux/macOS
   venv\Scripts\activate  # Windows
   ```

3. Instale as dependências:
   ```sh
   pip install -r requirements.txt
   ```

4. Configure as variáveis de ambiente criando um arquivo `.env`:
   ```sh
   DATABASE_URL=postgresql+psycopg2://usuario:senha@localhost:5432/nome_do_banco
   ```

5. Execute as migrações do banco de dados:
   ```sh
   alembic upgrade head
   ```

## Executando a API
Inicie o servidor FastAPI:
```sh
uvicorn main:app --reload
```
Acesse a documentação interativa em:
- [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs)

## Gerenciando Migrações com Alembic
Criar uma nova migração:
```sh
alembic revision --autogenerate -m "Mensagem da migração"
```
Aplicar migrações:
```sh
alembic upgrade head
```

## Endpoints Principais
### Empresas
- **GET /empresas/** - Lista todas as empresas
- **POST /empresas/** - Cria uma nova empresa
- **GET /empresas/{id}** - Busca uma empresa por ID
- **PUT /empresas/{id}** - Atualiza os dados de uma empresa
- **DELETE /empresas/{id}** - Remove uma empresa

## Contribuição
Sinta-se à vontade para contribuir com melhorias! Basta criar um fork do projeto e abrir um pull request.

