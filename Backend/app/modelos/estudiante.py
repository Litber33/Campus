from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.configuracion.conexion_mysql import Base

class Estudiante(Base):
    __tablename__ = 'estudiantes'
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    programa = Column(String(100))
    semestre = Column(Integer)

    usuario = relationship('Usuario', backref='estudiante')
