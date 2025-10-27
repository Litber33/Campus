from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.configuracion.conexion_mysql import obtener_db
from app.repositorios.repositorio_padres import crear_padre, obtener_padres, obtener_padre, actualizar_padre, eliminar_padre
from app.esquemas.padre_esquema import PadreCrear, PadreMostrar
from app.seguridad import rol_requerido

router = APIRouter(tags=['Padres'])

@router.get('/', response_model=list[PadreMostrar])
def listar(db: Session = Depends(obtener_db)):
    return obtener_padres(db)

@router.post('/', response_model=PadreMostrar, dependencies=[Depends(rol_requerido(['administrador']))])
def crear(datos: PadreCrear, db: Session = Depends(obtener_db)):
    return crear_padre(db, datos.dict())

@router.get('/{padre_id}', response_model=PadreMostrar)
def get_padre(padre_id: int, db: Session = Depends(obtener_db)):
    p = obtener_padre(db, padre_id)
    if not p:
        raise HTTPException(status_code=404, detail='Padre no encontrado')
    return p

@router.put('/{padre_id}', response_model=PadreMostrar, dependencies=[Depends(rol_requerido(['administrador']))])
def actualizar(padre_id: int, datos: PadreCrear, db: Session = Depends(obtener_db)):
    updated = actualizar_padre(db, padre_id, datos.dict())
    if not updated:
        raise HTTPException(status_code=404, detail='Padre no encontrado')
    return updated

@router.delete('/{padre_id}', dependencies=[Depends(rol_requerido(['administrador']))])
def eliminar(padre_id: int, db: Session = Depends(obtener_db)):
    ok = eliminar_padre(db, padre_id)
    if not ok:
        raise HTTPException(status_code=404, detail='Padre no encontrado')
    return {'mensaje': 'Padre eliminado'}
