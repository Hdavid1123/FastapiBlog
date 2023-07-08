from fastapi import FastAPI
from pydantic import BaseModel
from http import HTTPStatus

app = FastAPI()

# Entidad user colocar en los modelos
class User(BaseModel):
    id: int
    name: str
    surname: str
    email: str
    age: int

user_list = [
    User(id=1, name="Brais", surname="Moure", email="moure@gmail.com",age=35),
    User(id=2,name="David",surname="Vergel",email="david@gmail.com",age=20)
]

@app.get("/users")
async def users():
    return user_list


@app.get("/user/{id}")
async def getUser(id:int):
    try:
        userById = filter(lambda user: user.id == id, user_list)
        return list(userById)[0]
    except:
        return {HTTPStatus.NO_CONTENT:"NO CONTENT"}
    
@app.get("/userquery/")
async def getUser(id:int):
    try:
        userById = filter(lambda user: user.id == id, user_list)
        return list(userById)[0]
    except:
        return {HTTPStatus.NO_CONTENT:"NO CONTENT"}