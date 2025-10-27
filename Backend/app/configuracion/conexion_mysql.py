from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from app.configuracion.variables_entorno import DB_USER, DB_PASS, DB_HOST, DB_NAME, DB_PORT

DATABASE_URL = f'mysql+pymysql://{DB_USER}:{DB_PASS}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

engine = create_engine(DATABASE_URL, echo=False, pool_pre_ping=True)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
Base = declarative_base()

def obtener_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

def crear_tablas():
    # Importa los modelos para registrarlos en Base.metadata
    from app.modelos import usuario, estudiante, profesor, padre, administrador  # noqa
    Base.metadata.create_all(bind=engine)
