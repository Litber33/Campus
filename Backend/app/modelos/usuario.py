from sqlalchemy import Column, Integer, String, Enum
from app.configuracion.conexion_mysql import Base
import enum

class RolUsuario(enum.Enum):
    estudiante = 'estudiante'
    profesor = 'profesor'
    padre = 'padre'
    administrador = 'administrador'

class Usuario(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    correo = Column(String(150), unique=True, index=True, nullable=False)
    contrasena = Column(String(255), nullable=False)
    rol = Column(Enum(RolUsuario), nullable=False)
    