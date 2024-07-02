from fastapi import FastAPI
from fastapi.responses import HTMLResponse #Libreria para generar respuestas HTML
from config.database import engine, Base
from middlewares.error_handler import ErrorHandler
from routers.movie import movie_router
from routers.computadora import compu_router
from routers.user import user_router

app = FastAPI() #Nombre de instancia de api
app.title = "Mi Primera API"
app.version = "0.0.1"

app.add_middleware(ErrorHandler)

# ---------- BASE DE DATOS -----------
#Inicializa tu base de datos y crear las tablas necesarias basadas en los modelos que has definido
# Base.metadata.drop_all(engine)
Base.metadata.create_all(bind = engine)

#Ejecutar con uvicorn main:app --reload --port2000

@app.get('/', tags=["Home"])#Crear un endpoint con @ y nombre de la api
def message():
    return HTMLResponse('<h1> Holiiis :). </h1>')

app.include_router(user_router)
#app.include_router(movie_router)
app.include_router(compu_router)