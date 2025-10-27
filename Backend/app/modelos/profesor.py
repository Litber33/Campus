from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.configuracion.conexion_mysql import Base

class Profesor(Base):
    __tablename__ = 'profesores'
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    departamento = Column(String(100))
    titulo = Column(String(100))

    usuario = relationship('Usuario', backref='profesor')
    # Puedes agregar más atributos específicos del profesor aquí    
    