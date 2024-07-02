from fastapi import APIRouter, Path, Query, Depends
from fastapi.responses import JSONResponse #Libreria para generar respuestas HTML y de tipo JSON
from typing import List #Libreria para dar la opcion de dejar opcional un parametro del BaseModel
from config.database import Session
from models.movie import Movie as MovieModel
from fastapi.encoders import jsonable_encoder #Para convertir a JSON
from middlewares.jwt_bearer import JWTBearer
from services.movie import MovieService
from schemas.movie import Movie

movie_router = APIRouter()

#Endpoints Movies
#-------------------------#

#Endpoint que obtiene todas las movies
@movie_router.get('/Movies', tags=['Movies'], response_model=list[Movie], status_code=200)
def get_movies() -> List[Movie]:
    db = Session()
    result = MovieService(db).get_movies()
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

#Endpoint que regresa una movie por su id
@movie_router.get('/Movies/{id}', tags=['Movies'], response_model=Movie, status_code=200)
def get_movie(id : int = Path(ge=1, le=2000)) -> Movie :
    db = Session()
    result = MovieService(db).get_movies_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=404 ,content=jsonable_encoder(result))

#Endpoint que obtiene movies por su categoria
@movie_router.get('/Movies/', tags=['Movies'], response_model=List[Movie], status_code=200)
def get_movies_by_category(category : str = Query(min_length=5, max_length=15)): #Especifica lo que le tienes que mandar para poder
    db = Session()
    result = MovieService(db).get_movies_by_category(category)
    return JSONResponse(content=jsonable_encoder(result), status_code=200)
    
#Endpoint que crea una movie
@movie_router.post('/Movies/', tags=['Movies'], response_model=dict, status_code=200)
def create_movie(movie: Movie):
    db = Session()
    MovieService(db).create_movie(movie)
    return JSONResponse(content={"message": "Se ha registrado la pelicula"}, status_code=200)

#Endpoint que modifica una movie ya creada
@movie_router.put('/Movies/{id}', tags=['Movies'], status_code=200)
def update_movie(id: int, movie: Movie):
    db = Session()
    updated_movie = MovieService(db).update_movie(id, movie)
    if not updated_movie:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la pelicula"})

#Endpoint que elimina una movie mediante su id
@movie_router.delete('/Movies/{id}', tags=['Movies'], status_code=200)
def delete_movie(id: int):
    db = Session()
    result = MovieService(db).get_movies_by_id(id)
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    MovieService(db).delete_movie(id)
    return JSONResponse(status_code=200, content={"message": "Se eliminó la película"})
