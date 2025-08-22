#Arquivo que vai verificar a saude da API
from fastapi import APIRouter

router = APIRouter()
@router.get("/health")
def health_check():
    return {"Status": "healther"}