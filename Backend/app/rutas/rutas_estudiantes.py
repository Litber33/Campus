from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.configuracion.conexion_mysql import obtener_db
from app.repositorios.repositorio_estudiantes import crear_estudiante, obtener_estudiantes, obtener_estudiante, actualizar_estudiante, eliminar_estudiante
from app.esquemas.estudiante_esquema import EstudianteCrear, EstudianteMostrar
from app.seguridad import rol_requerido

router = APIRouter(tags=['Estudiantes'])

@router.get('/', response_model=list[EstudianteMostrar])
def listar(db: Session = Depends(obtener_db)):
    return obtener_estudiantes(db)

@router.post('/', response_model=EstudianteMostrar, dependencies=[Depends(rol_requerido(['administrador','profesor']))])
def crear(datos: EstudianteCrear, db: Session = Depends(obtener_db)):
    creado = crear_estudiante(db, datos.dict())
    return creado

@router.get('/{estudiante_id}', response_model=EstudianteMostrar)
def get_estudiante(estudiante_id: int, db: Session = Depends(obtener_db)):
    est = obtener_estudiante(db, estudiante_id)
    if not est:
        raise HTTPException(status_code=404, detail='Estudiante no encontrado')
    return est

@router.put('/{estudiante_id}', response_model=EstudianteMostrar, dependencies=[Depends(rol_requerido(['administrador']))])
def actualizar(estudiante_id: int, datos: EstudianteCrear, db: Session = Depends(obtener_db)):
    updated = actualizar_estudiante(db, estudiante_id, datos.dict())
    if not updated:
        raise HTTPException(status_code=404, detail='Estudiante no encontrado')
    return updated

@router.delete('/{estudiante_id}', dependencies=[Depends(rol_requerido(['administrador']))])
def eliminar(estudiante_id: int, db: Session = Depends(obtener_db)):
    ok = eliminar_estudiante(db, estudiante_id)
    if not ok:
        raise HTTPException(status_code=404, detail='Estudiante no encontrado')
    return {'mensaje': 'Estudiante eliminado'}
