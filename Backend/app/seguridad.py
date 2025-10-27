from passlib.context import CryptContext
from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session
from app.configuracion.variables_entorno import SECRET_KEY, ALGORITHM, ACCESS_TOKEN_EXPIRE_MINUTES
from app.configuracion.conexion_mysql import obtener_db
from app.modelos.usuario import Usuario

pwd_context = CryptContext(schemes=['bcrypt'], deprecated='auto')
oauth2_scheme = OAuth2PasswordBearer(tokenUrl='/api/auth/token')

def encriptar_clave(password: str):
    return pwd_context.hash(password)

def verificar_clave(plain, hashed):
    return pwd_context.verify(plain, hashed)

def crear_token(data: dict, expires_minutes: int = ACCESS_TOKEN_EXPIRE_MINUTES):
    to_encode = data.copy()
    expire = datetime.utcnow() + timedelta(minutes=expires_minutes)
    to_encode.update({'exp': expire})
    encoded = jwt.encode(to_encode, SECRET_KEY, algorithm=ALGORITHM)
    return encoded

def verificar_token(token: str = Depends(oauth2_scheme)):
    credentials_exception = HTTPException(
        status_code=status.HTTP_401_UNAUTHORIZED,
        detail='No se pudo validar las credenciales',
        headers={'WWW-Authenticate': 'Bearer'},
    )
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        correo: str = payload.get('sub')
        if correo is None:
            raise credentials_exception
        return payload
    except JWTError:
        raise credentials_exception

def obtener_usuario_actual(payload: dict = Depends(verificar_token), db: Session = Depends(obtener_db)):
    correo = payload.get('sub')
    user = db.query(Usuario).filter(Usuario.correo == correo).first()
    if not user:
        raise HTTPException(status_code=401, detail='Usuario no encontrado')
    return user

def rol_requerido(roles: list):
    def wrapper(user: Usuario = Depends(obtener_usuario_actual)):
        if user.rol.value not in roles:
            raise HTTPException(status_code=403, detail='No tiene permiso para realizar esta acción')
        return user
    return wrapper
