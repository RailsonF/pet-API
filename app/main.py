#Arquivo principal da aplicação 
from fastapi import FastAPI
from app.core.config import settings
from app.routes import health

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION
)

#Importando as rotas
app.include_router(health.router)

#Arquivo que vai verificar a saude da API
#Serve para carregar as configurações da aplicação a partir de variáveis de ambiente ou de um arquivo .env




