from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.configuracion.conexion_mysql import obtener_db
from app.repositorios.repositorio_profesores import crear_profesor, obtener_profesores, obtener_profesor, actualizar_profesor, eliminar_profesor
from app.esquemas.profesor_esquema import ProfesorCrear, ProfesorMostrar
from app.seguridad import rol_requerido

router = APIRouter(tags=['Profesores'])

@router.get('/', response_model=list[ProfesorMostrar])
def listar(db: Session = Depends(obtener_db)):
    return obtener_profesores(db)

@router.post('/', response_model=ProfesorMostrar, dependencies=[Depends(rol_requerido(['administrador']))])
def crear(datos: ProfesorCrear, db: Session = Depends(obtener_db)):
    return crear_profesor(db, datos.dict())

@router.get('/{profesor_id}', response_model=ProfesorMostrar)
def get_profesor(profesor_id: int, db: Session = Depends(obtener_db)):
    p = obtener_profesor(db, profesor_id)
    if not p:
        raise HTTPException(status_code=404, detail='Profesor no encontrado')
    return p

@router.put('/{profesor_id}', response_model=ProfesorMostrar, dependencies=[Depends(rol_requerido(['administrador']))])
def actualizar(profesor_id: int, datos: ProfesorCrear, db: Session = Depends(obtener_db)):
    updated = actualizar_profesor(db, profesor_id, datos.dict())
    if not updated:
        raise HTTPException(status_code=404, detail='Profesor no encontrado')
    return updated

@router.delete('/{profesor_id}', dependencies=[Depends(rol_requerido(['administrador']))])
def eliminar(profesor_id: int, db: Session = Depends(obtener_db)):
    ok = eliminar_profesor(db, profesor_id)
    if not ok:
        raise HTTPException(status_code=404, detail='Profesor no encontrado')
    return {'mensaje': 'Profesor eliminado'}
