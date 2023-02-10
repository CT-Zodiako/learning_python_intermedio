from fastapi import FastAPI
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
@app.post("/user/")
async def new_user(user: User):
    if type(search_user(user.id)) == User:
        return {"Error": "Ya existe"}
    else:
        users_list.append(user)

#put
@app.put("/user/")
async def user_update(user: User):
    for index,save_user in enumerate(users_list):
        if save_user.id == user == id:
            users_list[index] = user

#Function search
def search_user(id : int):
    users = filter(lambda user: user.id == id, users_list)
    try:
        return list(users)[0]
    except:
        return {"Error": "No se ecuentra el usuario"}
