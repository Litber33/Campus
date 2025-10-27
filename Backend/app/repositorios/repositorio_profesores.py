from sqlalchemy.orm import Session
from app.modelos.profesor import Profesor

def crear_profesor(db: Session, datos: dict):
    nuevo = Profesor(**datos)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_profesores(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Profesor).offset(skip).limit(limit).all()

def obtener_profesor(db: Session, profesor_id: int):
    return db.query(Profesor).get(profesor_id)

def actualizar_profesor(db: Session, profesor_id: int, datos: dict):
    p = db.query(Profesor).get(profesor_id)
    if not p:
        return None
    for key, value in datos.items():
        setattr(p, key, value)
    db.commit()
    db.refresh(p)
    return p

def eliminar_profesor(db: Session, profesor_id: int):
    p = db.query(Profesor).get(profesor_id)
    if p:
        db.delete(p)
        db.commit()
        return True
    return False
