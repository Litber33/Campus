Backend Campus Virtual (FastAPI)
-------------------------------
Instrucciones rápidas:
1. Crear la base de datos ejecutando backend/app/sql/campus_virtual.sql en MySQL.
2. Configurar backend/.env con tus credenciales MySQL.
3. Crear y activar un entorno virtual, luego instalar dependencias:
   pip install -r requirements.txt
4. Ejecutar el servidor:
   uvicorn main:app --reload
5. Documentación automática en:
   http://localhost:8000/docs