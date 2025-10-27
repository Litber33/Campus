from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.configuracion.conexion_mysql import Base

class Administrador(Base):
    __tablename__ = 'administradores'
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    cargo = Column(String(100))

    usuario = relationship('Usuario', backref='administrador')
    # Puedes agregar más atributos específicos del administrador aquí