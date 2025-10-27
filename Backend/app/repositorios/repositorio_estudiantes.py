from sqlalchemy.orm import Session
from app.modelos.estudiante import Estudiante

def crear_estudiante(db: Session, datos: dict):
    nuevo = Estudiante(**datos)
    db.add(nuevo)
    db.commit()
    db.refresh(nuevo)
    return nuevo

def obtener_estudiantes(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Estudiante).offset(skip).limit(limit).all()

def obtener_estudiante(db: Session, estudiante_id: int):
    return db.query(Estudiante).get(estudiante_id)

def actualizar_estudiante(db: Session, estudiante_id: int, datos: dict):
    est = db.query(Estudiante).get(estudiante_id)
    if not est:
        return None
    for key, value in datos.items():
        setattr(est, key, value)
    db.commit()
    db.refresh(est)
    return est

def eliminar_estudiante(db: Session, estudiante_id: int):
    est = db.query(Estudiante).get(estudiante_id)
    if est:
        db.delete(est)
        db.commit()
        return True
    return False
