from fastapi import FastAPI
from routers import productos, user
from fastapi.staticfiles import StaticFiles


app = FastAPI()

app.include_router(productos.router)
app.include_router(user.router)


app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/")
async def root():
    return "!Hello"

@app.get("/User")
async def name(name):
    name = name
    return {
        "nombre":"F{name}",
        "apellido":"Tovar"
    }

