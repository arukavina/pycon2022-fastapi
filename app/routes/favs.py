#from app.crud import favs
from app.models.favs import FavoriteSongDB, FavoriteSongCreate

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def root():
    return {"message": "Ugh... Hello, World!"}
