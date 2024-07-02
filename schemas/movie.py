from typing import Optional #Libreria para dar la opcion de dejar opcional un parametro del BaseModel
from pydantic import BaseModel, Field #Libreria para crear un modelo base para despues modificar


class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=1, max_length=15)
    overview: str = Field(min_length=1, max_length=50)
    year : int = Field(default=2000, le=2024)#le == lest or equal menor o igual
    rating : float = Field(ge=1.0, le=10)
    category : str = Field(min_length=1, max_length=15)

    class Config:
        json_schema_extra={
            "example": {
                "id" : 1,
                "title": "Mi Pelicula",
                "overview": "Descripción de pelicula",
                "year": 2024,
                "rating": 10.0,
                "category": "Acción"
            }
        }