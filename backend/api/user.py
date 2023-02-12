from fastapi import FastAPI, HTTPException
from pydantic import BaseModel

app = FastAPI()

# Entidad user


class User(BaseModel):  # parametrisa la clase
    id : int
    name: str
    surname: str
    age: int


users_list = [User(id=1, name="Cristian", surname="Tovar", age=24),
              User(id=2, name="Cristian", surname="Pancho", age=24),
              User(id=3, name="Paco", surname="Flaca", age=24)]


@app.get("/usersJson")  # hecho a mano
async def user():
    return [
        {"name": "Cristian", "surname": "Tovar", "age": 24},
        {"name": "Cristian", "surname": "Pancho", "age": 44},
        {"name": "Juan", "surname": "Idrobo", "age": 33}
    ]


@app.get("/users")
async def users():
    return users_list

#Path
@app.get("/user/{id}")
async def user(id: int):
    return search_user(id)

#Query
@app.get("/user/")
async def user(id: int):
    return search_user(id)

#post
@app.post("/user/",status_code=201)
async def new_user(user: User):
    if type(search_user(user.id)) == User:
        raise HTTPException(status_code=404, detail="Ya existe")
    else:
        users_list.append(user)
        return user

#put
@app.put("/user/")
async def user_update(user: User):
    found = False
    for index,save_user in enumerate(users_list):
        if save_user.id == user.id:
            users_list[index] = user
            found = True
    if not found:
        return {"error"}
    else:
        return user

#delete
@app.delete("/user/{id}")
async def user_delete(id: int):
    found = False
    for index,save_user in enumerate(users_list):
        if save_user.id == id:
            del users_list[index]
            found = True
    if not found:
        return {"No econtrado para eliminar"}
    else:
        return {"ELIMINADO"}

#Function search
def search_user(id : int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error": "No se ecuentra el usuario"}
