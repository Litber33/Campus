from fastapi import FastAPI
from app.rutas import rutas_estudiantes, rutas_profesores, rutas_padres, rutas_administradores, rutas_autenticacion
from app.configuracion.conexion_mysql import crear_tablas
from fastapi.middleware.cors import CORSMiddleware

app = FastAPI(title="Campus Virtual", version="1.0")

# Configurar CORS (para conectar con el frontend en React)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Crear tablas si no existen
crear_tablas()

# Registrar rutas
app.include_router(rutas_autenticacion.router)
app.include_router(rutas_estudiantes.router)
app.include_router(rutas_profesores.router)
app.include_router(rutas_padres.router)
app.include_router(rutas_administradores.router)

@app.get("/")
def inicio():
    return {"mensaje": "API del Campus Virtual funcionando correctamente "}