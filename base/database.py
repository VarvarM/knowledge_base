from sqlalchemy import create_engine, text, insert
from base.config import settings
from sqlalchemy.orm import sessionmaker, declarative_base

engine = create_engine(url=settings.DATABASE_URL_psycopg)
SessionLocal = sessionmaker(autoflush=False, bind=engine)

