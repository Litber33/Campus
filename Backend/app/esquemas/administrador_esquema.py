from pydantic import BaseModel

class AdministradorBase(BaseModel):
    usuario_id: int
    cargo: str | None = None

class AdministradorCrear(AdministradorBase):
    pass

class AdministradorMostrar(AdministradorBase):
    id: int
    class Config:
        orm_mode = True
