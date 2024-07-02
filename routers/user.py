from fastapi import APIRouter
from fastapi.responses import JSONResponse #Libreria para generar respuestas HTML y de tipo JSON
from fastapi.responses import JSONResponse #Libreria para generar respuestas HTML y de tipo JSON
from utils.jwt_manager import create_token #Metodos previamente creados en el jwt_manager.py
from schemas.user import User


user_router = APIRouter()


#Endpoint que genera un token para validar credenciales
@user_router.post('/login', tags=['Authorization'])
def login(user: User):
    if user.email == "admin@gmail.com" and user.password == "admin":
        token: str = create_token(dict(user))
        return JSONResponse(status_code=200, content=token)
