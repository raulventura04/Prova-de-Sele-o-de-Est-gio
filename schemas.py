from pydantic import BaseModel, EmailStr

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str
    email: EmailStr
    telefone: str

class EmpresaCreate(EmpresaBase):
    pass

class EmpresaResponse(EmpresaBase):
    id: int
    class Config:
        from_attributes = True

class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str
    empresa_id: int

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    pass

class ObrigacaoAcessoriaResponse(ObrigacaoAcessoriaBase):
    id: int
    class Config:
        from_attributes = True