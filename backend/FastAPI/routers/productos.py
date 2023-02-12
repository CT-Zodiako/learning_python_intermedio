from fastapi import APIRouter

router = APIRouter(prefix="/products",
                   tags=["products"],
                   responses = {404:{"message": "No encotrado"}})


productos_list = ["Uno","Dos","Tres","Cuatro"]

@router.get("/")
async def prodcuts():
        return productos_list

@router.get("/{id}")
async def prodcuts(id: int):
        return productos_list[id]
