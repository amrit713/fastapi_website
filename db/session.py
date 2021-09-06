from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from typing import Generator

from core.config import settings

# SQLALCHEMY_DATABASE_URL= settings.SQLALCHEMY_DATABASE_URL

# engine = create_engine(SQLALCHEMY_DATABASE_URL,echo=True)

SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"

engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread":False}
)

sessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

def get_db() ->Generator:
    try:
        db = sessionLocal()
        yield db

    finally:
        db.close()