import os
from pathlib import Path
from dotenv import load_dotenv

env_path = Path('.')/".env"
load_dotenv(dotenv_path=env_path)

class Settings:
    PROJECT_TITLE:str = "Jobobard"
    PROJECT_VERSION:str = "0.1.1"

    POSTGRES_USER:str = os.getenv("POSTGRES_USER")
    POSTGRES_PASSWORD= os.getenv("POSTGRES_PASSWORD")
    POSTGRES_SERVER= os.getenv("POSTGRES_SERVER","localhost")
    POSTGRES_PORT= os.getenv("POSTGRES_PORT", 5432)
    POSTGRES_DB= os.getenv("POSTGRES_DB", "fastapi_db")

    SQLALCHEMY_DATABASE_URL = f"postgres://{POSTGRES_USER}:{POSTGRES_PASSWORD}@{POSTGRES_SERVER}/{POSTGRES_DB}"
   



settings =Settings()