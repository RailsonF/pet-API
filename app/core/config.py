#configurações globais da aplicação
from pydantic import BaseSettings, SettingsConfigDict
class Settings(BaseSettings):
    APP_NAME: str = "Pet API"
    API_VERSION: str = "1.0.0"

    model_config = SettingsConfigDict(
        env_file=".env", env_file_encoding="utf-8"
    )
    #Para que serve esse arquivo?
    #Serve para carregar as configurações da aplicação a partir de variáveis de ambiente ou de
settings = Settings()    
