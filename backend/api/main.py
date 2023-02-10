from fastapi import FastAPI

app = FastAPI()


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

