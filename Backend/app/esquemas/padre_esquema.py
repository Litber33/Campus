from pydantic import BaseModel

class PadreBase(BaseModel):
    usuario_id: int
    telefono: str | None = None
    direccion: str | None = None

class PadreCrear(PadreBase):
    pass

class PadreMostrar(PadreBase):
    id: int
    class Config:
        orm_mode = True
