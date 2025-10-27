from sqlalchemy.orm import Session
from app.modelos.padre import Padre

def crear_padre(db: Session, datos: dict):
    nuevo = Padre(**datos)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_padres(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Padre).offset(skip).limit(limit).all()

def obtener_padre(db: Session, padre_id: int):
    return db.query(Padre).get(padre_id)

def actualizar_padre(db: Session, padre_id: int, datos: dict):
    p = db.query(Padre).get(padre_id)
    if not p:
        return None
    for key, value in datos.items():
        setattr(p, key, value)
    db.commit()
    db.refresh(p)
    return p

def eliminar_padre(db: Session, padre_id: int):
    p = db.query(Padre).get(padre_id)
    if p:
        db.delete(p)
        db.commit()
        return True
    return False
