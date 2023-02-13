from fastapi import FastAPI, HTTPException, Depends,status
from pydantic import BaseModel
from fastapi.security import OAuth2PasswordBearer, OAuth2PasswordRequestForm

app = FastAPI()
oauth2_scheme = OAuth2PasswordBearer(tokenUrl="login")



class User(BaseModel):
    username: str
    full_name: str
    email: str
    disabled : bool

class UserDB(User):
    password: str

users_db = {
    "zodiako": {
        "username":"zodiako",
        "full_name":"Cristian Tovar",
        "email":"cristian@gmail.com",
        "disabled": False,
        "password": "123456"
    },
    "zodiako2": {
        "username":"zodiako2",
        "full_name":"Cristian2 Tovar2",
        "email":"cristian2@gmail.com",
        "disabled": True,
        "password": "7654321"
    }
}

def search_user(username: str):
    if username in users_db:
        return UserDB(**users_db[username])

async def current_user(token:str = Depends(oauth2_scheme)):
    user = search_user(token)
    if not user:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Credenciales de autentifiacion invalidas", headers={"WWW-Authenticate":"Bearer"})

@app.post("/login")
async def login(form: OAuth2PasswordRequestForm = Depends()):
    user_db = users_db.get(form.username)
    if not user_db:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="EL usuario no es correcto")
    user = search_user(form.username)

    if not form.password == user.password:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Contraseña inorrecta")
    return {"access_token": user.username,"token_type":"bearer"}

@app.get("/users/me`")
async def me(user: User = Depends(current_user)):
    return user