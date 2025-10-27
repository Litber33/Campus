from sqlalchemy.orm import Session
from app.modelos.usuario import Usuario, RolUsuario

def crear_usuario(db: Session, datos: dict):
    nuevo = Usuario(
        nombre=datos['nombre'],
        correo=datos['correo'],
        contrasena=datos['contrasena'],
        rol=RolUsuario(datos['rol'])
    )
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_usuario_por_correo(db: Session, correo: str):
    return db.query(Usuario).filter(Usuario.correo == correo).first()

def listar_usuarios(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Usuario).offset(skip).limit(limit).all()

def eliminar_usuario(db: Session, usuario_id: int):
    user = db.query(Usuario).get(usuario_id)
    if user:
        db.delete(user)
        db.commit()
        return True
    return False
