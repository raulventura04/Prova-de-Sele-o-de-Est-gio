import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from database import Base, get_db
from main import app
import os

# Criar um banco de dados temporário para os testes
TEST_DATABASE_URL = "sqlite:///./test.db"

# Criar engine e sessão para o banco de testes
engine = create_engine(TEST_DATABASE_URL, connect_args={"check_same_thread": False})
TestSessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Criar as tabelas no banco de testes antes de rodar os testes
Base.metadata.create_all(bind=engine)

@pytest.fixture
def db():
    """Cria uma sessão para testes e fecha ao final."""
    session = TestSessionLocal()
    try:
        yield session
    finally:
        session.close()

# Substitui a dependência do banco de dados no app pelo de testes
app.dependency_overrides[get_db] = db

# Cliente de testes
client = TestClient(app)

def test_create_empresa():
    response = client.post("/empresas/", json={
        "nome": "Empresa Teste",
        "cnpj": "12345678000195",
        "endereco": "Rua Teste, 123",
        "email": "empresa@teste.com",
        "telefone": "11999999999"
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "Empresa Teste"

def test_get_empresas():
    response = client.get("/empresas/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)

def test_create_obrigacao():
    # Criar empresa antes, pois Obrigacao precisa de empresa_id válido
    client.post("/empresas/", json={
        "nome": "Empresa Teste",
        "cnpj": "12345678000195",
        "endereco": "Rua Teste, 123",
        "email": "empresa@teste.com",
        "telefone": "11999999999"
    })

    response = client.post("/obrigacoes/", json={
        "nome": "DCTF",
        "periodicidade": "mensal",
        "empresa_id": 1
    })
    assert response.status_code == 200
    assert response.json()["nome"] == "DCTF"

def test_get_obrigacoes():
    response = client.get("/obrigacoes/")
    assert response.status_code == 200
    assert isinstance(response.json(), list)
