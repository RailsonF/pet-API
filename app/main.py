#Arquivo principal da aplicação 
#FastAPI
from fastapi import FastAPI
from app.core.config import settings
from app.routes import health

app = FastAPI(
    title=settings.APP_NAME,
    version=settings.API_VERSION
)
#Importando as rotas
app.include_router(health.router, prefix="/health", tags=["health"])
#Arquivo que vai verificar a saude da API --- IGNORE ---
#Serve para carregar as configurações da aplicação a partir de variáveis de ambiente ou de um arquivo .env
#Isso permite que as configurações sejam facilmente alteradas sem precisar modificar o código-fonte.
# um arquivo .env
#Isso permite que as configurações sejam facilmente alteradas sem precisar modificar o código-fonte.

