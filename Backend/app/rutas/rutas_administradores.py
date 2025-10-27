from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from app.configuracion.conexion_mysql import obtener_db
from app.repositorios.repositorio_usuarios import listar_usuarios, eliminar_usuario
from app.seguridad import rol_requerido

router = APIRouter(tags=['Administradores'])

@router.get('/usuarios', dependencies=[Depends(rol_requerido(['administrador']))])
def listar(db: Session = Depends(obtener_db)):
    return listar_usuarios(db)

@router.delete('/usuarios/{usuario_id}', dependencies=[Depends(rol_requerido(['administrador']))])
def eliminar(usuario_id: int, db: Session = Depends(obtener_db)):
    ok = eliminar_usuario(db, usuario_id)
    if not ok:
        raise HTTPException(status_code=404, detail='Usuario no encontrado')
    return {'mensaje': 'Usuario eliminado'}
