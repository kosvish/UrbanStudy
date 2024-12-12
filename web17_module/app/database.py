from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import sqlite3

SQLALCHEMY_DATABASE_URL = "sqlite:///./library.db"

engine = create_engine(SQLALCHEMY_DATABASE_URL, echo=True, pool_size=10, max_overflow=20)
SessionLocal = sessionmaker(bind=engine)

Base = declarative_base()

session = SessionLocal()


# Генератор сессий
def get_db():
    session = SessionLocal()
    try:
        yield session
    finally:
        session.close()
