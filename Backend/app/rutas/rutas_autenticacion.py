from fastapi import APIRouter, Depends, HTTPException, status
from sqlalchemy.orm import Session
from app.configuracion.conexion_mysql import obtener_db
from app.repositorios.repositorio_usuarios import crear_usuario, obtener_usuario_por_correo
from app.esquemas.usuario_esquema import UsuarioCrear, UsuarioMostrar
from app.seguridad import encriptar_clave, verificar_clave, crear_token

router = APIRouter(tags=['Autenticacion'])

@router.post('/registro', response_model=UsuarioMostrar)
def registro(usuario: UsuarioCrear, db: Session = Depends(obtener_db)):
    if obtener_usuario_por_correo(db, usuario.correo):
        raise HTTPException(status_code=400, detail='Correo ya registrado')
    datos = usuario.dict()
    # en el esquema el campo se llama 'contrasena'
    datos['contrasena'] = encriptar_clave(datos.pop('contrasena'))
    nuevo = crear_usuario(db, {'nombre': datos['nombre'], 'correo': datos['correo'], 'contrasena': datos['contrasena'], 'rol': datos['rol']})
    return nuevo

@router.post('/login')
def login(correo: str, contrasena: str, db: Session = Depends(obtener_db)):
    user = obtener_usuario_por_correo(db, correo)
    if not user or not verificar_clave(contrasena, user.contrasena):
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail='Credenciales invalidas')
    token = crear_token({'sub': user.correo, 'rol': user.rol.value})
    return {'access_token': token, 'token_type': 'bearer', 'rol': user.rol.value, 'usuario_id': user.id}
