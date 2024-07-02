from config.database import Base
from sqlalchemy import Column, Integer, String, Float

class Computadora(Base):

    __tablename__="computadoras"

    Id = Column(Integer, primary_key = True)
    Marca = Column(String)
    Modelo = Column(String)
    Color = Column(String)
    Ram = Column(Integer)
    Almacenamiento = Column(String)