from pydantic_settings import BaseSettings
from pathlib import Path

class Settings(BaseSettings):
    DB_USER:str

    DB_PASSWORD:str

    DB_PORT:int

    DB_HOST:str

    DB_NAME:str


    class Config:
        env_file = Path(__file__).parent / ".env"
        case_sensitive = True
        extra = "forbid"
        validate_assignment = True
        allow_mutation = False



settings = Settings()