# B2B Platform API - V2

Esta é uma API robusta desenvolvida com **FastAPI** para gestão de empresas e usuários em um cenário B2B, focada em performance, segurança e organização de dados.

## 🚀 Tecnologias Utilizadas
- **Python 3.12+**
- **FastAPI**: Framework de alta performance.
- **SQLAlchemy**: ORM para gestão do banco de dados SQLite.
- **Bcrypt**: Criptografia de senhas (Segurança da Informação).
- **Pydantic**: Validação rigorosa de Schemas.

## 🛠️ Funcionalidades Implementadas
- **CRUD de Empresas**: Cadastro e listagem de organizações.
- **Relacionamento de Dados**: Vínculo inteligente entre Usuários e Empresas (Foreign Keys).
- **Segurança Sênior**: Hashing de senhas para proteção de dados sensíveis.
- **Documentação Automática**: Swagger UI interativo disponível em `/docs`.

## 📦 Como Executar o Projeto
1. Clone o repositório.
2. Crie um ambiente virtual: `python -m venv venv`.
3. Instale as dependências: `pip install -r requirements.txt`.
4. Inicie o servidor: `python -m uvicorn app.main:app --reload`.
