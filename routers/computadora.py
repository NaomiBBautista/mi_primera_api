from fastapi import APIRouter, Depends
from fastapi.responses import JSONResponse #Libreria para generar respuestas HTML y de tipo JSON
from typing import Optional, List #Libreria para dar la opcion de dejar opcional un parametro del BaseModel
from pydantic import BaseModel, Field #Libreria para crear un modelo base para despues modificar
from config.database import Session
from models.computadora import Computadora as CompuModel
from fastapi.encoders import jsonable_encoder #Para convertir a JSON
from middlewares.jwt_bearer import JWTBearer

compu_router = APIRouter()

class Computadora(BaseModel):
    Id: Optional[int] = None
    Marca: str = Field(min_length=1, max_length=20)
    Modelo: str = Field(min_length=1, max_length=20)
    Color : str = Field(min_length=1, max_length=20)
    Ram : int = Field(default=8, le=128)#le == lest or equal menor o igual
    Almacenamiento : str = Field(min_length=1, max_length=10)
    #Modelo que sirve como Ejemplo 
    class Config:
        json_schema_extra={
            "example": {
                "Id" : 1,
                "Marca": "Marca de tu compu",
                "Modelo": "Modelo de tu compu",
                "Color": "Color de tu compu",
                "Ram": 8,
                "Almacenamiento": "256 GB"
            }
        }


#Endpoints de Computadoras
# ------------#
#Endpoint para obtener todas las computadoras
@compu_router.get('/Computadoras', tags=['Computadoras'], response_model=List[Computadora], status_code=200)
def get_Computadoras() -> List[Computadora]:
    db = Session() #Crea una sesion para conectarnos a la DB
    result = db.query(CompuModel).all() #Querry que obtiene todo en la db
    return JSONResponse(content=jsonable_encoder(result), status_code=200)

#Endpoint para obtener una computadora mediante su Id
@compu_router.get('/Computadoras/{id}', tags=['Computadoras'], status_code=200)
def get_Computadoras_by_id(id : int):
    db = Session()
    result = db.query(CompuModel).filter(CompuModel.Id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    return JSONResponse(status_code=200, content= jsonable_encoder(result))

#Endpoint para obtener todas las computadoras por marca
@compu_router.get('/Computadoras/', tags=['Computadoras'], status_code=200)
def get_computadoras_by_marca(marca : str):
    db = Session() #Crea una sesion para conectarnos a la DB
    result = db.query(CompuModel).filter(CompuModel.Marca == marca).all()
    return JSONResponse(content= jsonable_encoder(result), status_code=200)

#Endpoint para crear una computadora
@compu_router.post('/Computadoras/', tags=['Computadoras'], response_model=dict, status_code=200)
def create_computadora(compu: Computadora):
    db = Session()
    new_compu = CompuModel(**compu.model_dump())#Utiliza el modelo de la clase Computadora
    db.add(new_compu)
    db.commit()
    return JSONResponse(content={"message": "Se ha registrado la computadora correctamente"}, status_code=200)

#Endpoint para modificar una computadora ya existente
@compu_router.put('/Computadoras/{id}', tags=['Computadoras'], status_code=200)
def update_Computadoras(id: int, compu: Computadora):
    db = Session()
    result = db.query(CompuModel).filter(CompuModel.Id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    result.Marca = compu.Marca
    result.Modelo = compu.Modelo
    result.Color = compu.Color
    result.Ram = compu.Ram
    result.Almacenamiento = compu.Almacenamiento
    db.commit()
    return JSONResponse(status_code=200, content={"message": "Se ha modificado la pelicula"})

#Endpoint para eliminar una computadora ya existente
@compu_router.delete('/Computadoras/{id}', tags=['Computadoras'], status_code=200)
def delete_Computadoras(id: int):
    db = Session()
    result = db.query(CompuModel).filter(CompuModel.Id == id).first()
    if not result:
        return JSONResponse(status_code=404, content={'message': "No encontrado"})
    db.delete(result)
    db.commit()
    return JSONResponse(status_code=200, content={'message': "Se elimino la computadora"}) 