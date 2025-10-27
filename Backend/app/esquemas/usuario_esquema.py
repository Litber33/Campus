from pydantic import BaseModel, EmailStr
from enum import Enum

class RolUsuario(str, Enum):
    estudiante = 'estudiante'
    profesor = 'profesor'
    padre = 'padre'
    administrador = 'administrador'

class UsuarioBase(BaseModel):
    nombre: str
    correo: EmailStr
    rol: RolUsuario

class UsuarioCrear(UsuarioBase):
    contrasena: str

class UsuarioMostrar(UsuarioBase):
    id: int
    class Config:
        orm_mode = True
