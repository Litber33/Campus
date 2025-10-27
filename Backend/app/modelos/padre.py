from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from app.configuracion.conexion_mysql import Base

class Padre(Base):
    __tablename__ = 'padres'
    id = Column(Integer, primary_key=True, index=True)
    usuario_id = Column(Integer, ForeignKey('usuarios.id'), nullable=False)
    telefono = Column(String(30))
    direccion = Column(String(100))

    usuario = relationship('Usuario', backref='padre')
    # Puedes agregar más atributos específicos del padre aquí