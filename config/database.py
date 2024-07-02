#importa funciones para leer directorios y manipular rutas de archivos.
import os
#Para crear un motor de base de datos
from sqlalchemy import create_engine
#Para crear una sesion temporal a la DB
from sqlalchemy.orm.session import sessionmaker
#Para crear tablas con clases en py
from sqlalchemy.ext.declarative import declarative_base

#Le da el nobre al archivo
sqlite_file_name = "../database.sqlite" 

#Estamos leyendo el directorio actual
base_dir = os.path.dirname(os.path.realpath(__file__))

#Creamos la url de la base de datos uniendo las 2 variables anteriores
database_url = f"sqlite:///{os.path.join(base_dir, sqlite_file_name)}"

#Crea el motor para la base de datos
engine = create_engine(database_url, echo = True)

#crea una clase que vamos a usar para conectarnos a la DB
Session = sessionmaker(bind=engine)

#Lo usamos para definir la estructura de nuestras tablas
Base = declarative_base()