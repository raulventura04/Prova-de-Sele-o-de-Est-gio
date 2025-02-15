from sqlalchemy.orm import Session
import models, schemas

def create_empresa(db: Session, empresa: schemas.EmpresaCreate) -> models.Empresa:
    db_empresa = models.Empresa(**empresa.model_dump())
    db.add(db_empresa)
    db.commit()
    db.refresh(db_empresa)
    return db_empresa

def get_empresas(db: Session) -> list[models.Empresa]:
    return db.query(models.Empresa).all()

def create_obrigacao(db: Session, obrigacao: schemas.ObrigacaoAcessoriaCreate) -> models.ObrigacaoAcessoria:
    db_obrigacao = models.ObrigacaoAcessoria(**obrigacao.model_dump())
    db.add(db_obrigacao)
    db.commit()
    db.refresh(db_obrigacao)
    return db_obrigacao

def get_obrigacoes(db: Session) -> list[models.ObrigacaoAcessoria]:
    return db.query(models.ObrigacaoAcessoria).all()