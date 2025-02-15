from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import models, schemas, crud

app = FastAPI()

@app.post("/empresas/", response_model=schemas.EmpresaResponse)
def create_empresa(empresa: schemas.EmpresaCreate, db: Session = Depends(get_db)):
    return crud.create_empresa(db=db, empresa=empresa)

@app.get("/empresas/", response_model=list[schemas.EmpresaResponse])
def read_empresas(db: Session = Depends(get_db)):
    return crud.get_empresas(db)

@app.post("/obrigacoes/", response_model=schemas.ObrigacaoAcessoriaResponse)
def create_obrigacao(obrigacao: schemas.ObrigacaoAcessoriaCreate, db: Session = Depends(get_db)):
    return crud.create_obrigacao(db=db, obrigacao=obrigacao)

@app.get("/obrigacoes/", response_model=list[schemas.ObrigacaoAcessoriaResponse])
def read_obrigacoes(db: Session = Depends(get_db)):
    return crud.get_obrigacoes(db)

