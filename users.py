from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

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

# Path
@app.get("/user/{id}")
async def get_user(id:int):
   return search_user(id)

# Query
@app.get("/user/")
async def get_user(id:int):
        return search_user(id)
    
def search_user(id:int):
    try:
        userById = filter(lambda user: user.id == id, user_list)
        return list(userById)[0]
    except:
        raise HTTPException(status_code=204, detail="User doesn't exist")

@app.post("/user/", status_code=201)
async def create_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=204, detail="User already exists")
    user_list.append(user)
    return user


@app.put("/user/", status_code=201)
async def update_user(user: User):
    found = False

    for index, savedUser in enumerate(user_list):
        if savedUser.id == user.id:
            user_list[index] == user
            found = True
    
    if not found:
        raise HTTPException(status_code=204, detail="User doesn't exist")
    return user


@app.delete("/user/{id}")
async def delete_user(id:int):
    found = False

    for index, savedUser in enumerate(user_list):
        if savedUser.id == id:
            del user_list[index]
            found = True
        
    if not found:
        return {"Error":"User doesn't exist"}
            