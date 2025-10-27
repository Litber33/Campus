from pydantic import BaseModel

class EstudianteBase(BaseModel):
    usuario_id: int
    programa: str | None = None
    semestre: int | None = None

class EstudianteCrear(EstudianteBase):
    pass

class EstudianteMostrar(EstudianteBase):
    id: int
    class Config:
        orm_mode = True
