from pydantic import BaseModel

class ProfesorBase(BaseModel):
    usuario_id: int
    departamento: str | None = None
    titulo: str | None = None

class ProfesorCrear(ProfesorBase):
    pass

class ProfesorMostrar(ProfesorBase):
    id: int
    class Config:
        orm_mode = True
